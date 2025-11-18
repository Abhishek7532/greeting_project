from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello! Welcome to the Greeting API"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello {name}, nice to meet you!"}
