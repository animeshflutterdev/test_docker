from fastapi import FastAPI
from redis_client import redis_client
from mongo_client import db

app = FastAPI()

@app.get("/")
def read_root():
    redis_client.set("health", "ok")
    return {"Hello": "World"}

@app.get("/f")
def f():
    health_data = redis_client.get("health")
    return {"Hello": f" --- {health_data} ---"}

@app.get("/mongo-test")
def mongo_test():
    col = db.health
    col.insert_one({"status": "ok"})
    return {"count": col.count_documents({})}