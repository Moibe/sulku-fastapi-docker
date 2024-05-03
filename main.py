from fastapi import FastAPI
import funciones

app = FastAPI()

@app.get("/")
def hello(): 

    return {"Status":"Deployed"}

@app.get("/getTokens/{userfile}")
def getTokens(userfile: str):
    tokens = funciones.getAccess(userfile)
    print("Tipo de resultado:", type(tokens))
    return tokens

@app.get("/debitTokens/{userfile}/{work}")
def debitTokens(userfile: str, work: str):
    tokens = funciones.debitTokens(userfile,work) 
    print("Tipo de resultado:", type(tokens))
    return tokens