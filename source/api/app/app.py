from typing import Union

from fastapi import FastAPI, HTTPException

from .v1.itinary.itinary_gen import ItinaryGenerator
from .v1.itinary.itinary_models import ItinaryCreationSchema, ItinaryCreationResponseSchema
from .v1.poi import InputPoiClass, get_poi_by_class, PoiListSchema
from .v1.poi.poi_detail_model import get_poi_detail, PoiDetailSchema

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/poi/{poi_id}", response_model=Union[PoiDetailSchema, None])
def get_poi(poi_id: str):
    poi = get_poi_detail(poi_id)
    if poi is None:
        raise HTTPException(status_code=404, detail="Poi not found")
    return poi

@app.get("/poi_by_class/{classname}", response_model=Union[PoiListSchema, None])
def get_poi_for_class(classname: str):
    poi = get_poi_by_class(InputPoiClass(classname=classname))
    if poi is None:
        raise HTTPException(status_code=404, detail="Poi not found")
    return poi

@app.post("/itinary/")
def create_itinary(payload: ItinaryCreationSchema) -> ItinaryCreationResponseSchema:
    igen = ItinaryGenerator()
    return igen.create_itinary(payload)

@app.get("/itinary/{itinary_id}")
def get_itinary(itinary_id: int):
    res = get_itinary(itinary_id)
    return res
