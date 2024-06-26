from fastapi import FastAPI
import funciones

app = FastAPI()

@app.get("/")
def start(): 

    return {"Status":"Deployed"}

## GET TOKENS ##

#Vía Path
@app.get("/getTokens/{userfile}")
def getTokens(userfile: str):
    tokens = funciones.getTokens(userfile)
    print("Tipo de resultado:", type(tokens))
    return tokens

#Vía Query 
@app.get("/getTokensQ/")
def getTokens(userfile: str = "gAAAAABmEZA4SLBC2YczouOrjIEi9WNCNGOIvyUcqBUnzxNsftXTdy54KaX9x8mAjFkABSI6FJrdZDQKk_5lpJOgJoMChxlniw=="):
    tokens = funciones.getTokens(userfile)
    print("Tipo de resultado:", type(tokens))
    return tokens

## AUTHORIZE WORK ##

#Vía Parameters
@app.get("/authorize/{tokens}/{work}")
def getTokens(tokens: int, work: str):
    autorizacion = funciones.authorize(tokens, work)
    print("Tipo de resultado:", type(autorizacion))
    return autorizacion

#Vía Query
@app.get("/authorizeQ/")
def debitTokens(tokens: int, work: str = "picswap"):
    autorizacion = funciones.authorize(tokens,work) 
    print("Tipo de resultado:", type(autorizacion))
    return autorizacion


## DEBIT TOKENS ##

#Vía Parámeters
@app.get("/debitTokens/{userfile}/{work}")
def debitTokens(userfile: str, work: str):
    tokens = funciones.debitTokens(userfile,work) 
    print("Tipo de resultado:", type(tokens))
    return tokens

#Vía Query
@app.get("/debitTokensQ/")
def debitTokens(userfile: str, work: str = "picswap"):
    tokens = funciones.debitTokens(userfile,work) 
    print("Tipo de resultado:", type(tokens))
    return tokens