from fastapi import FastAPI
from pymongo import MongoClient
from api.controller.user_controller import user
from dotenv import load_dotenv
from contextlib import asynccontextmanager

import time
import logging
import os


load_dotenv()
mongodb_uri = os.getenv("MONGODB_URI")
database_name = os.getenv("DATABASE_NAME")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(mongodb_uri)
    app.database = app.mongodb_client[database_name]
    yield
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(user, prefix="/api")


@app.middleware("http")
async def add_process_time_header(request, call_next):
    logger.info("Adding process time header")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Process time: {process_time}")
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/health")
def health():
    return {"status": "UP"}
