from fastapi import FastAPI
import funciones

app = FastAPI()

@app.get("/")
def start(): 

    return {"Status":"Deployed"}

@app.get("/getTokens/{userfile}")
def getTokens(userfile: str):
    tokens = funciones.getAccess(userfile)
    print("Tipo de resultado:", type(tokens))
    return tokens

@app.get("/getTokensQ/")
def getTokens(userfile: str = "gAAAAABmEZA4SLBC2YczouOrjIEi9WNCNGOIvyUcqBUnzxNsftXTdy54KaX9x8mAjFkABSI6FJrdZDQKk_5lpJOgJoMChxlniw=="):
    tokens = funciones.getAccess(userfile)
    print("Tipo de resultado:", type(tokens))
    return tokens

@app.get("/debitTokens/{userfile}/{work}")
def debitTokens(userfile: str, work: str):
    tokens = funciones.debitTokens(userfile,work) 
    print("Tipo de resultado:", type(tokens))
    return tokens

@app.get("/debitTokensQ/")
def debitTokens(userfile: str, work: str = "picswap"):
    tokens = funciones.debitTokens(userfile,work) 
    print("Tipo de resultado:", type(tokens))
    return tokens