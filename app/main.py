from logging import getLogger
from json import dumps, loads

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models

logger = getLogger("uvicorn")

app = FastAPI(title = 'LT crypto services API v2')

@app.on_event("startup")
async def startup_event():
  app.add_middleware(CORSMiddleware, allow_origins = ["*"], allow_credentials = True, allow_methods = ["*"], allow_headers=["*"])

@app.get("/ping")
async def ping():
  return {"response": "pong"}

@app.post("/prescription")
async def prescription(data: models.Prescription) -> models.Prescription:
  logger.info(dumps(data.dict(), indent = 2))
  return data

  with open("./galleries.json") as f:
    json = loads(f.read())
  return json[context]