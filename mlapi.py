from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import json

app = FastAPI()

class House(BaseModel):
    location: str
    sqft: int
    bath:int
    bhk:int

with open("columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:] 

with open('model.pkl','rb') as f:
    model = pickle.load(f)


@app.post('/')
async def scoring_endpoint(item: House):
    inputdict = item.dict()
    try:
        loc_index = data_columns.index(inputdict["location"].lower())
    except:
        loc_index = -1
    x = np.zeros(len(data_columns))
    x[0] = inputdict["sqft"]
    x[1] = inputdict["bath"]
    x[2] = inputdict["bhk"]
    if loc_index >= 0:
        x[loc_index] = 1
    pred = round(model.predict([x])[0],2) * 100000
    return {"prediction":pred}
