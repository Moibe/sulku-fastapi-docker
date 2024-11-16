import funciones
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def start(): 
    return {"Status":"Deployed"}

## GET DATA (USERS) ##
#Vía Path
@app.get("/getData/{aplicacion}")
def getData(aplicacion: str):
    print("La app que recibí es: ", aplicacion)
    data = funciones.getData(aplicacion)    
    return data

#Vía Query 
@app.get("/getDataQ/")
def getData(aplicacion: str):
    data = funciones.getData(aplicacion)
    return data

## GET TOKENS ##
#Vía Path
@app.get("/getTokens/{userfile}/{env}")
def getTokens(userfile: str, env: str):
    tokens = funciones.getTokens(userfile, env)
    return tokens

#Vía Query 
@app.get("/getTokensQ/")
def getTokens(userfile: str = "gAAAAABmEZA4SLBC2YczouOrjIEi9WNCNGOIvyUcqBUnzxNsftXTdy54KaX9x8mAjFkABSI6FJrdZDQKk_5lpJOgJoMChxlniw==", env: str = "dev"):
    tokens = funciones.getTokens(userfile, env)
    return tokens

## AUTHORIZE WORK ##
#Vía Parameters
@app.get("/authorize/{tokens}/{work}")
def authorize(tokens: int, work: str):
    autorizacion = funciones.authorize(tokens, work)
    return autorizacion

#Vía Query
@app.get("/authorizeQ/")
def authorize(tokens: int, work: str = "picswap"):
    autorizacion = funciones.authorize(tokens,work) 
    #print("Tipo de resultado:", type(autorizacion))
    return autorizacion


## DEBIT TOKENS ##
#Vía Parámeters
@app.get("/debitTokens/{userfile}/{work}")
def debitTokens(userfile: str, work: str):
    tokens = funciones.debitTokens(userfile,work) 
    #print("Tipo de resultado:", type(tokens))
    return tokens

#Vía Query
@app.get("/debitTokensQ/")
def debitTokens(userfile: str, work: str = "picswap"):
    tokens = funciones.debitTokens(userfile,work) 
    #print("Tipo de resultado:", type(tokens))
    return tokens

## GET USER Novelty ##
#Vía Parámeters
@app.get("/getUserNovelty/{userfile}")
def getUserNovelty(userfile: str):
    novelty = funciones.getUserNovelty(userfile) 
    #print("Tipo de resultado:", type(novelty))
    return novelty

#Vía Query
@app.get("/getUserNovelty/")
def getUserNovelty(userfile: str):
    novelty = funciones.getUserNovelty(userfile) 
    #print("Tipo de resultado:", type(novelty))
    return novelty