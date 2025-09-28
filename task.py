from fastapi import FastAPI

app = FastAPI()

@app.get("/add/{a}/{b}")
async def add(a:int,b:int):
    return {"sum": a+b}



@app.get("/sub/{a}/{b}")
async def sub(a:int,b:int):
    return {"sub": a-b}


