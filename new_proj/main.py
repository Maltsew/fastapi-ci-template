"""
main module docstring
"""
from fastapi import FastAPI
from pydantic import BaseModel
from .settings import settings


app = FastAPI()


class Status(BaseModel):
    """
    class status
    """
    status: str = "OK"


@app.get(settings.main_url)
async def status() -> Status:
    """
    func status
    :return: Coroutine[Any, Any, Status]
    """
    return Status()
