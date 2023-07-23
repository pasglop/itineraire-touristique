from array import array
from typing import List

from pydantic import BaseModel, Field, RootModel

poi_detail_example = {
                "id": 1,
                "name": "Tour Eiffel",
                "website": "https://www.toureiffel.paris/fr",
                "latitude": 48.85837009999999,
                "longitude": 2.2944813,
                "address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
                "phone": "01 44 11 23 23",
                "description": "La tour Eiffel est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.",
                "classname": [
                    {
                        "id": 1,
                        "name": "tour",
                        "type": "TOUR"
                    },
                    {
                        "id": 2,
                        "name": "monument",
                        "type": "MONUMENT"
                    }
                ]
            }

class PoiClass(BaseModel):
    id: int
    name: str
    type: str
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "tour"
            }
        }

class PoiClassList(RootModel):
    root: List[PoiClass]

class PoiDetailSchema(BaseModel):
    id: int
    name: str
    website: str
    latitude: float
    longitude: float
    address: str
    phone: str
    description: str
    classname: PoiClassList
    class Config:
        schema_extra = {
            "example": poi_detail_example
        }