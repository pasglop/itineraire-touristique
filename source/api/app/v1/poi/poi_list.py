from typing import List

from pydantic import BaseModel

from .poi_detail_model import PoiDetailSchema, get_poi_sql, poi_detail_example
from ..utils.db import connect_db


# a model for input one class and get poi list
class PoiListSchema(BaseModel):
    poi : List[PoiDetailSchema]

    class Config:
        json_schema_extra = {
            "poi" : [
                poi_detail_example
            ]}

# a model for input one class and get poi list
class InputPoiClass(BaseModel):
    classname : str



def get_poi_by_class(classname: InputPoiClass) -> PoiListSchema:
    conn, cursor = connect_db()
    cursor.execute(get_poi_sql("c.type = %s and a.locality = 'Paris'"), (classname.classname,))
    poi = cursor.fetchall()
    for i in range(len(poi)):
        poi[i] = dict(poi[i])
    return PoiListSchema(poi=poi)