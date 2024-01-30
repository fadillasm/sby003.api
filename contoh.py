from fastapi import FastAPI, HTTPException, Header
import pandas as pd

df = pd.read_csv('Financials.csv')

app = FastAPI()

API_KEY = "testingAPI1234"

@app.get("/")
def home():
    return {'Message':'This is my API. Welcome'}

@app.get("/protected/{pos}")
def protect(pos:str, api_key:str=Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    else:
        return df[df['Country']==pos].to_dict(orient='records')