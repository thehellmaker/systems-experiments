from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    text: str

TORCHSERVE_URL = "http://localhost:9080/predictions/bert_classifier"

@app.get("/ping")
def health_check():
    response = requests.get("http://localhost:9080/ping")
    return {"torchserve_status": response.json()}

@app.post("/invocations")
def predict(data: InputData):
    payload = {"text": data.text}
    response = requests.post(TORCHSERVE_URL, json=payload)
    return response.json()
