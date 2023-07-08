from logging import getLogger
from json import dumps

from fastapi import FastAPI

from models import Collection

logger = getLogger("uvicorn")

app = FastAPI()

@app.get("/ping")
async def ping():
  return {"response": "pong"}

@app.get("/collection")
async def collection(data: Collection) -> Collection:
  logger.info(dumps(data.dict(), indent = 2))
  return data
