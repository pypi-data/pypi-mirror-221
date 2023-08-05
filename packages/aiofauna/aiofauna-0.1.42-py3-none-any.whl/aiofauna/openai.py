import asyncio
import json
import os
from abc import ABC, abstractmethod
from typing import Dict, List, Literal, Optional, Type, TypeVar, Union
from uuid import uuid4

from dotenv import load_dotenv
from jinja2 import Template
from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

from .client import HTTPException, make_client
from .logging import setup_logging

load_dotenv()
logger = setup_logging(__name__)
Model = Literal["gpt-4-0613", "gpt-3.5-turbo-16k-0613"]
pinecone = make_client(base_url=os.environ["PINECONE_BASE_URL"], headers={"api-key": os.environ["PINECONE_API_KEY"]})
openai = make_client(base_url=os.environ["OPENAI_BASE_URL"], headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"})

Vector = List[float]
MetaData = Dict[str, str]

class UpsertVector(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    values:Vector = Field(...)
    metadata: MetaData = Field(...)
    
class UpsertRequest(BaseModel):
    vectors: List[UpsertVector] = Field(..., max_items=100)
    namespace:str = Field(...)
    
class UpsertResponse(BaseModel):
    upsertedCount: int = Field(...)
    
class QueryRequest(BaseModel):
    topK: int = Field(default=4, description="The number of results to return")
    namespace: str = Field(...)
    vector: Vector = Field(...)
    includeMetadata: bool = Field(default=True, description="Whether to include metadata in the response")
    
class QueryMatch(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    score: float = Field(...)
    values: Vector = Field(...)
    metadata: MetaData = Field(...)
    
class QueryResponse(BaseModel):
    matches: List[QueryMatch] = Field(...)
    namespace: str = Field(...)

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
    model: Model = Field(default="gpt-4-0613")
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


async def handle_errors(func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)
    except HTTPException as e:
        logger.error(e.__class__.__name__)
        logger.error(e.reason)
        raise e
    except Exception as e:
        logger.error(e.__class__.__name__)
        logger.error(str(e))
        raise e


async def upsert_vectors(request: UpsertRequest) -> UpsertResponse:
    response = await handle_errors(pinecone.fetch, "/vectors/upsert", method="POST", json=request.dict(exclude_none=True))
    return UpsertResponse(**response)
    
async def query_vectors(request: QueryRequest) -> QueryResponse:
    response = await handle_errors(pinecone.fetch, "/vectors/query", method="POST", json=request.dict(exclude_none=True))
    #logger.info(response)
    return QueryResponse(**response)

async def create_embedding(request: CreateEmbeddingRequest) -> CreateEmbeddingResponse:
    response = await handle_errors(openai.fetch, "/v1/embeddings", method="POST", json=request.dict(exclude_none=True))
    return CreateEmbeddingResponse(**response)

async def create_chat_completion(request: CreateChatCompletionRequest) -> CreateChatCompletionResponse:
    response = await handle_errors(openai.fetch, "/v1/chat/completions", method="POST", json=request.dict(exclude_none=True))
    return CreateChatCompletionResponse(**response)

async def create_user_message(prompt: str):
    return ChatCompletionRequestMessage(role="user", content=prompt)

async def create_system_message(context:Optional[str]=None):
    if context is None:
        context = "I am a bot"
    return ChatCompletionRequestMessage(role="system", content=context)

async def create_chat_request(messages:List[ChatCompletionRequestMessage]):
    return CreateChatCompletionRequest(messages=messages)

async def get_previous_statements(user_embedding:Vector, namespace:str="default"):
    query_request = QueryRequest(vector=user_embedding, namespace=namespace)
    query_response = await query_vectors(query_request)
    return [i.metadata["text"] for i in query_response.matches]

async def create_retrieval_template(previous:List[str],template= Template("The previous statements were:\n{% for i in previous %}{{i}}\n{% endfor %}")):
    return await template.render_async(previous=previous)

async def get_chat_completion(chat_completion_request):
    response = await create_chat_completion(chat_completion_request)
    text = response.choices[0].message.content
    assert isinstance(text, str)
    return text
    
async def get_embeddings(text):
    embedding_request = CreateEmbeddingRequest(input=text)
    embedding_response = await create_embedding(embedding_request)
    return embedding_response.data[0].embedding

async def upser_vectors(user_embedding, openai_embedding, prompt, text, namespace):
    upsert_request = UpsertRequest(
        vectors=[
            UpsertVector(values=user_embedding, metadata={"text": prompt}),
            UpsertVector(values=openai_embedding, metadata={"text": text})
        ],
        namespace=namespace
    )
    await upsert_vectors(upsert_request)

async def chat_completion(prompt: str, namespace: str="default", retrieval:bool=True, context:Optional[str]=None) -> str:
    try:
        user_message = await create_user_message(prompt)
        if retrieval:
            embedding_request = CreateEmbeddingRequest(input=prompt)
            embedding_response = await create_embedding(embedding_request)
            user_embedding = embedding_response.data[0].embedding
            previous = await get_previous_statements(user_embedding, namespace)
            previous = await create_retrieval_template(previous)
            system_message = await create_system_message(previous)
        else:
            system_message = await create_system_message(context)

        chat_completion_request = await create_chat_request([system_message, user_message])
        text = await get_chat_completion(chat_completion_request)
        if retrieval:
            user_embedding = await get_embeddings(prompt)
            openai_embedding = await get_embeddings(text)
            await upser_vectors(user_embedding, openai_embedding, prompt, text, namespace)
        return text
    except HTTPException as e:
        logger.error(e.__class__.__name__)
        logger.error(e.reason)
        raise e
    except Exception as e:
        logger.error(e.__class__.__name__)
        logger.error(str(e))
        raise e
    
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
    async def run(self):
        pass
    
F = TypeVar("F", bound=FunctionType)
    
async def function_call(text:str,functions:List[Type[F]]):
    data = {
        "model": "gpt-4-0613",
        "messages":[{
                "role": "user",
                "content": text
            }],
        "functions": [i.openaischema for i in functions]
    }
    
    response = await openai.post("/v1/chat/completions", json=data)
    logger.info("Response: %s", response)
    if "function_call" in response['choices'][0]['message']:
        call_struct = response['choices'][0]['message']['function_call']
        name = call_struct['name']
        logger.info("Function name: %s", name)
        arguments = call_struct['arguments']
        logger.info("Function arguments: %s", arguments)
        for i in functions:
            if i.__name__ == name:
                instance = i(**json.loads(arguments))
                result = await instance.run()
                logger.info("Function result: %s", result)
                break
        else:
            raise ValueError(f"Function {name} not found")
        return result
    return response['choices'][0]['message']['content']

async def chat_chain(text:str, context:Optional[str]=None, retrieval=False, iterations:int=8):
    texts = []
    for i in range(iterations):
        text = await chat_completion(prompt=text, context=context, retrieval=retrieval)
        texts.append(text)
        await asyncio.sleep(0.1)
    return texts