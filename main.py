from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "hello world"}

@app.get("/ping")
def get_root():
    return {"message": "pong"}
