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
    return autorizacion


## DEBIT TOKENS ##
#Vía Parámeters
@app.get("/debitTokens/{userfile}/{work}/{env}")
def debitTokens(userfile: str, work: str, env: str):
    tokens = funciones.debitTokens(userfile,work, env)
    return tokens

#Vía Query
@app.get("/debitTokensQ/")
def debitTokens(userfile: str, work: str = "picswap", env: str = "dev"):
    tokens = funciones.debitTokens(userfile,work, env) 
    return tokens

## CONTROL QUOTA ##
#Vía Parámeters
@app.get("/getQuota/")
def getQuota():
    quota = funciones.getQuota() 
    return quota

#Vía Query
@app.get("/getQuota/")
def getQuota():
    quota = funciones.getQuota() 
    return quota

#Vía Parámeters
@app.get("/updateQuota/{costo_proceso}")
def updateQuota(costo_proceso: int):
    quota = funciones.updateQuota(costo_proceso) 
    return quota

#Vía Query
@app.get("/updateQuota/")
def updateQuota(costo_proceso: int):
    quota = funciones.updateQuota(costo_proceso) 
    return quota

## GET USER Novelty ##
#Vía Parámeters
@app.get("/getUserNovelty/{userfile}/{aplicacion}")
def getUserNovelty(userfile: str, aplicacion: str):
    novelty = funciones.getUserNovelty(userfile, aplicacion) 
    return novelty

#Vía Query
@app.get("/getUserNovelty/")
def getUserNovelty(userfile: str, aplicacion: str):
    novelty = funciones.getUserNovelty(userfile, aplicacion) 
    return novelty