import fastapi
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from yamlloader import data

app = FastAPI()

@app.post("/")
async def senden():
    pass

@app.get("/")
async def fromdata(data): 
    if data.Users[0].value == "testUser1":
        print(data.Users[0])
    else:
        print("error")
        
