
"""
This file contains the itinary blueprint.
will be rendered through API as a json array
each object in the array will be a step of the itinary

"""
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from ..poi import PoiDetailSchema, poi_detail_example


class StepTypeEnum(str, Enum):
    walk = 'Marcher'
    subway = 'Prendre le métro'
    eat = 'Manger'
    visit = 'Visiter'

class WalkDetailSchema(BaseModel):
    name: str
    distance: float
    duration: float
    start_latitude: float
    start_longitude: float
    end_latitude: float
    end_longitude: float

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Marcher jusqu'à la tour Eiffel",
                "distance": 100,
                "duration": 3,
                "start_latitude": 48.85836,
                "start_longitude": 2.294543,
                "end_latitude": 48.85836,
                "end_longitude": 2.294543
            }
        }

class SubwayDetailSchema(BaseModel):
    name: str
    duration: float
    line: str
    direction: str
    nb_stations: int
    final_station: str
    list_station: list[str]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Prendre la ligne 6 direction Charles de Gaulle Etoile",
                "duration": 14,
                "line": "6",
                "direction": "Charles de Gaulle Etoile",
                "nb_stations": 10
            }
        }

class EatDetailSchema(BaseModel):
    name: str
    latitude: float
    longitude: float
    duration: float = 60

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Manger autour de la tour Eiffel",
                "latitude": 48.85836,
                "longitude": 2.294543,
                "duration": 60
            }
        }

class VisitDetailSchema(PoiDetailSchema):
    duration: float = 60

    class Config:
        poi_visit_example = poi_detail_example.copy()
        poi_visit_example["duration"] = 60
        json_schema_extra = {
            "example": poi_visit_example
        }


class ItinaryStepGenericSchema(BaseModel):
        step: int
        name: str
        step_type: StepTypeEnum
        step_detail: VisitDetailSchema | EatDetailSchema | SubwayDetailSchema | WalkDetailSchema
        instruction: str
        comment: Optional[str] = None

class ItinaryStepVisitSchema(ItinaryStepGenericSchema):
    step_type: StepTypeEnum = StepTypeEnum.visit
    step_detail: VisitDetailSchema

    class Config:
        poi_visit_example = poi_detail_example.copy()
        poi_visit_example["duration"] = 60
        json_schema_extra = {
                "example": {
                    "step": 1,
                    "name": "Tour Eiffel",
                    "step_type": StepTypeEnum.visit,
                    "step_detail": poi_visit_example,
                    "instruction": "Prendre le métro",
                    "comment": "La Tour Eiffel, créée par Gustave Eiffel pour l'Exposition universelle de Paris de 1889, est devenue le symbole de la capitale française et un site touristique de premier plan : il s'agit du second site culturel français payant le plus visité en 2011, avec 7,1 millions de visiteurs dont 75 % d'étrangers en 2011, la cathédrale Notre-Dame de Paris étant en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés en 2011."
                }
            }

class ItinaryStepWalkSchema(ItinaryStepGenericSchema):
    step_type: StepTypeEnum = StepTypeEnum.walk
    step_detail: WalkDetailSchema


class ItinaryStepSubwaySchema(ItinaryStepGenericSchema):
    step_type: StepTypeEnum = StepTypeEnum.subway
    step_detail: SubwayDetailSchema

class ItinaryStepEatSchema(ItinaryStepGenericSchema):
    step_type: StepTypeEnum = StepTypeEnum.eat
    step_detail: EatDetailSchema


class ItinarySchema(BaseModel):
    steps: list[ItinaryStepEatSchema | ItinaryStepSubwaySchema | ItinaryStepVisitSchema | ItinaryStepWalkSchema]

class ItinarySchemaDays(BaseModel):
    days: list[ItinarySchema]

class ItinaryCreationSchema(BaseModel):
    hotel_poi: str
    days: int

    class Config:
        json_extra_schema = {
            "example": {
                "hotel_poi": "ChIJMVd4Mymu5kcRrZ0YgYgurpM",
                "days": 2
            }
        }

class ItinaryCreationResponseSchema(BaseModel):
    itinary_id: int
    itinary: ItinarySchemaDays
