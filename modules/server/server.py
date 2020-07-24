from typing import Optional
from fastapi import FastAPI
import json

import addpath
from protocols import protocols as prt

app = FastAPI()

proto_obj = prt.Protocols(prt.Types.BGP, prt.Format.BIRD_1_x)

string = {"Protocols": proto_obj.list_protocol() }
print(string)

@app.get("/")
def read_root():
    return {"Bird API": {"Version": "1", "Author": "Vineeth Penugonda"}}

@app.get("/protocols")
def read_protocols():
    return string

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}