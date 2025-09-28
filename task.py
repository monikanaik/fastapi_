from fastapi import FastAPI

app = FastAPI()

@app.get("/add/{a}/{b}")
async def add(a:int,b:int):
    return {"sum": a+b}

@app.get("/sub/{a}/{b}")
async def sub(a:int,b:int):
    return {"sub": a-b}

@app.get("/mul/{a}/{b}")
async def mul(a:int,b:int):
    return {"mul": a*b}

@app.get("/div/{a}/{b}")
async def div(a:int,b:int):
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"div": a/b} 
