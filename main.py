
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI project"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
