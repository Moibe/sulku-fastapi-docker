from fastapi import FastAPI
import aplicacion 

app = FastAPI()

@app.get("/")
def hello(): 

    return {"Status":"Deployed"}

@app.get("/getTokens")
def getTokens(): 

    return {"Status":"Getting Tokens..."}

@app.get("/debitTokens")
def debitTokens(): 

    return {"Status":"Debitting tokens..."}