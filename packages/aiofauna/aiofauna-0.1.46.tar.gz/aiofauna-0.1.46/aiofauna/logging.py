import logging
import os
from datetime import datetime
from pathlib import Path

from aiohttp.web_exceptions import HTTPException
from rich.console import Console
from rich.logging import RichHandler
from rich.pretty import install
from rich.traceback import install as ins


def setup_logging(name) -> logging.Logger:
    """Set's up logging"""
    
    install()
    ins()
    
    console = Console(record=True, force_terminal=True)
    
    path = Path(os.getcwd()) / "logs"
    path.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(
        filename=f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log",
        mode="w",
        encoding="utf-8",
    )
    file_handler.setFormatter(logging.Formatter("%(message)s"))
    file_handler.setLevel(logging.INFO)
    console_handler = RichHandler(
        console=console,
        show_time=True,
        show_path=True,
        markup=True,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        tracebacks_extra_lines=5,
        tracebacks_theme="solarized",
    )
    console_handler.setFormatter(logging.Formatter("%(message)s"))
    console_handler.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    return logger

def handle_errors(func,logger: logging.Logger=setup_logging(__name__)):
    async def wrapper(*args, **kwargs):
        try:
            logger.info("Calling %s", func.__name__)
            return await func(*args, **kwargs)
        except HTTPException as e:
            logger.error(e.__class__.__name__)
            logger.error(e.reason)
            raise e
        except Exception as e:
            logger.error(e.__class__.__name__)
            logger.error(str(e))
            raise e
    return wrapper
