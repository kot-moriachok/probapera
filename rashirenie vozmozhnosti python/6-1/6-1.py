from pydantic import BaseModel
from fastapi import FastAPI

class Sallers(BaseModel):
    name: str
    address: str
    city: str

@app.get("/sallers/{saller_id}")
def get_sallers(saller_id: int, q: str = None):
    return {"saller_id": saller_id: q}

@app.get("/sallers/{saller_id}/update")
def update_sallers(saller_id: int, saller: Sallers):
    return {"saller_id": saller_id: q}

@app.post("/sallers")
def create_sallers(sallers: Sallers):
    return {"sallers": sallers}
