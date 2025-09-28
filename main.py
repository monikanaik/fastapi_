from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}   


@app.get("/item/{item_id}")
async def item(item_id: int):
    return {"Item Id": item_id} 


@app.get("/index")
async def index():
    return {"data": "Hello World"} 


@app.get("/home/{s}")
async def home(s:str):
    return {"data": f"{s}"} 

