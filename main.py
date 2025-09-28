from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}   

@app.get("/index")
async def index():
    return {"Hello": "World"} 
