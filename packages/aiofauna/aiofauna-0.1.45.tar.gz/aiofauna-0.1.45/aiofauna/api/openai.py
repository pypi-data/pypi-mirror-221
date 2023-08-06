import asyncio
import json
import os
from abc import ABC, abstractmethod
from typing import Any, List, Optional, Type, TypeVar, Union

from jinja2 import Template
from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

from ..logging import handle_errors, setup_logging
from .pinecone import (APIClient, APIConfig, PineconeClient, QueryRequest,
                       Vector, dataclass, field)

logger = setup_logging(__name__)

class CreateEmbeddingRequest(BaseModel):
    model: str = Field(default="text-embedding-ada-002", description="The model to use for embedding")
    input: Union[str, List[str], List[int], List[List[int]]] = Field(..., description="Input text to embed")
  
class EmbeddingData(BaseModel):
    index: int = Field(...)
    object: str = Field(...)
    embedding: List[float] = Field(...)

class Usage(BaseModel):
    prompt_tokens: int = Field(...)
    total_tokens: int = Field(...)

class CreateEmbeddingResponse(BaseModel):
    object: str = Field(...)
    model: str = Field(...)
    data: List[EmbeddingData] = Field(...)
    usage: Usage = Field(...)    

class ChatCompletionRequestMessage(BaseModel):
    role: str = Field(..., description="The role of the messages author.")
    content: Optional[str] = Field(default=None, description="The contents of the message.")

class ChatCompletionResponseMessage(BaseModel):
    index: int = Field(...)
    message: ChatCompletionRequestMessage = Field(...)
    finish_reason: str = Field(...)

class CreateChatCompletionRequest(BaseModel):
    model: str = Field(default="gpt-4-0613")
    messages: List[ChatCompletionRequestMessage] = Field(default_factory=list)
    temperature: float = Field(default=0.2)
    top_p: float = Field(default=1.0)
    n: int = Field(default=1)
    stream: bool = Field(default=False)
    stop: Optional[Union[str, List[str]]] = Field(default=None)
    max_tokens: int = Field(default=512)
    presence_penalty: float = Field(default=0.0)
    frequency_penalty: float = Field(default=0.0)
    logit_bias: Optional[dict] = Field(default=None)
   
    def __init__(self, **kwargs):
        try:
            super().__init__(**kwargs)
        except ValueError:
            logger.info("Model %s not accessible, using gpt-3.5-turbo-16k-0613", kwargs["model"])
            kwargs["model"] = "gpt-3.5-turbo-16k-0613"
            super().__init__(**kwargs)

class CreateChatCompletionResponse(BaseModel):
    id: str = Field(...)
    object: str = Field(...)
    created: int = Field(...)
    model: str = Field(...)
    choices: List[ChatCompletionResponseMessage] = Field(...)
    usage: Usage = Field(...)
    
@handle_errors
async def create_user_message(prompt:str):
    return ChatCompletionRequestMessage(role="user", content=prompt)

@handle_errors
async def create_system_message(context:str):
    return ChatCompletionRequestMessage(role="system", content=context)
@handle_errors
async def create_chat_request(messages):
    return CreateChatCompletionRequest(messages=messages)
@handle_errors
async def create_retrieval_template(previous):
    retrieval_template = Template("The previous statements were:\n{% for i in previous %}{{i}}\n{% endfor %}")
    return retrieval_template.render(previous=previous)

class FunctionType(BaseModel, ABC):
    @classmethod    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        schema = cls.schema()
        name = cls.__name__
        description = cls.__doc__
        if not description:
            raise ValueError(f"{name} must have a docstring")
        cls.openaischema = {
            "name": cls.__name__,
            "description":cls.__doc__,
            "parameters": {
                "type": "object",
                "properties": schema["properties"],
                "required": schema["required"]
            },
        }
   
    @abstractmethod
    async def run(self)->Any:
        ...
    
F = TypeVar("F", bound=FunctionType)
    

@dataclass
class OpenAIClient(APIClient):
    config:APIConfig = field(default=APIConfig(base_url="https://api.openai.com", headers={"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}", "Content-Type": "application/json"})) # type: ignore
    @handle_errors
    async def create_embedding(self,request: CreateEmbeddingRequest) -> CreateEmbeddingResponse:
        response = await self.fetch("/v1/embeddings", method="POST", json=request.dict(exclude_none=True))
        return CreateEmbeddingResponse(**response)

    @handle_errors
    async def create_chat_completion(self,request: CreateChatCompletionRequest) -> CreateChatCompletionResponse:
        response = await self.fetch("/v1/chat/completions", method="POST", json=request.dict(exclude_none=True))
        return CreateChatCompletionResponse(**response)
    @handle_errors
    async def get_previous_statements(self,pinecone:PineconeClient,user_embedding, namespace:str="default")->List[str]:
        query_request = QueryRequest(vector=user_embedding, namespace=namespace)
        query_response = await pinecone.query_vectors(query_request)
        return [i.metadata["text"] for i in query_response.matches]

    @handle_errors
    async def get_chat_response(self,chat_completion_request:CreateChatCompletionRequest)->str:
        text = await self.create_chat_completion(chat_completion_request)
        if isinstance(text, str):
            return text
        else:
            assert isinstance(text.choices[0].message.content, str)
            return text.choices[0].message.content

    @handle_errors
    async def get_embeddings(self,text:str)->Vector:
        embedding_request = CreateEmbeddingRequest(input=text)
        embedding_response = await self.create_embedding(embedding_request)
        return embedding_response.data[0].embedding
    @handle_errors
    async def chat_completion(self, prompt: str, pinecone:PineconeClient, namespace: str="default", retrieval:bool=True, context:Optional[str]=None) -> str:
        user_message = await create_user_message(prompt)
        if retrieval:
            user_embedding = await self.get_embeddings(prompt)
            previous = await self.get_previous_statements(pinecone, user_embedding, namespace)
            if len(previous) > 0:
                previous = await create_retrieval_template(previous)
                system_message = await create_system_message(previous)
                chat_completion_request = await create_chat_request([system_message, user_message])
            else:
                chat_completion_request = await create_chat_request([user_message])
        if isinstance(context, str):
            system_message = await create_system_message(context)
            chat_completion_request = await create_chat_request([system_message, user_message])
        else:    
            chat_completion_request = await create_chat_request([user_message])
        text = await self.get_chat_response(chat_completion_request)
        if retrieval:
            user_embedding = await self.get_embeddings(prompt)
            openai_embedding = await self.get_embeddings(text)
            await pinecone.upsert_vectors_to_pinecone(user_embedding, openai_embedding, prompt, text, namespace)
        return text

    @handle_errors
    async def function_call(self,text:str,functions:List[Type[F]]):
        data = {
            "model": "gpt-4-0613",
            "messages":[{
                    "role": "user",
                    "content": text
                }],
            "functions": [i.openaischema for i in functions]
        }
        
        response = await self.post("/v1/chat/completions", json=data)
        if "function_call" in response['choices'][0]['message']:
            call_struct = response['choices'][0]['message']['function_call']
            name = call_struct['name']
            logger.info("Function name: %s", name)
            arguments = call_struct['arguments']
            logger.info("Function arguments: %s", arguments)
            for i in functions:
                if i.__name__ == name:
                    result = await i.run(i(**json.loads(arguments)))
                    logger.info("Function result: %s", result)
                    break
            else:
                raise ValueError(f"Function {name} not found")
            return result
        else:
            return response['choices'][0]['message']['content']
    @handle_errors
    async def lang_chain(self,text:str, pinecone:PineconeClient, iterations:int=8):
        texts = []
        for i in range(iterations):
            text = await self.chat_completion(prompt=text,pinecone=pinecone, retrieval=False)
            texts.append(text)
            await asyncio.sleep(0.1)
        return texts