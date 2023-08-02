from typing import Union
import dotenv

from fastapi import FastAPI, HTTPException

dotenv.load_dotenv()
from .v1.itinary import itinary_gen
from .v1.itinary import itinary_models
from .v1.poi import poi_list, poi_detail_model

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/poi/{poi_id}", response_model=Union[poi_detail_model.PoiDetailSchema, None])
def get_poi(poi_id: str):
    poi = poi_detail_model.get_poi_detail(poi_id)
    if poi is None:
        raise HTTPException(status_code=404, detail="Poi not found")
    return poi

@app.get("/poi_by_class/{classname}", response_model=Union[poi_list.PoiListSchema, None])
def get_poi_for_class(classname: str):
    poi = poi_list.get_poi_by_class(poi_list.InputPoiClass(classname=classname))
    if poi is None:
        raise HTTPException(status_code=404, detail="Class not exists or no poi found")
    return poi

@app.post("/itinary/")
def create_itinary(payload: itinary_models.ItinaryCreationSchema) -> itinary_models.ItinaryCreationResponseSchema:
    igen = itinary_gen.ItinaryGenerator()
    res = igen.create_itinary(payload)
    return res

@app.get("/itinary/{itinary_id}")
def get_itinary(itinary_id: int):
    res = get_itinary(itinary_id)
    return res
