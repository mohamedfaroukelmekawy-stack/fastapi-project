from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI project"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}



class Message(BaseModel):
    text: str

@app.post("/echo")
def echo_message(message: Message):
    return {"response": message.text}