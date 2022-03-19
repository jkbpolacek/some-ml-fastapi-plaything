#!/usr/bin/env python3

from fastapi import FastAPI

from typing import List
from joblib import load

import pandas

import src.model as model

app = FastAPI(
    title="Titatnic ML API",
    description="API for titanic dataset ml model",
    version="1.0",
)


@app.on_event("startup")
async def load_model():
    model.clf = load("./model/model.joblib")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
async def predict(passengers: List[model.Passenger]):
    passengers = list(map(dict, passengers))
    print(passengers)
    df = pandas.DataFrame(passengers)
    print(df)
    predict = model.clf.predict(df)
    print(predict)
    return predict.tolist()
