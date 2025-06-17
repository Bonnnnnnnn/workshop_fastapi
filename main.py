from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/todos")
async def gettodos():
    return [
        {"id": 1, "detail": "first todos"},
        {"id": 2, "detail": "second todos"}
    ] 

counter = 0
@app.get("/counter")
async def get_counter():
    global counter
    counter += 1
    return {"message" : f"counter = {counter}"}    