from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def print_hw():
    return "hello world"
