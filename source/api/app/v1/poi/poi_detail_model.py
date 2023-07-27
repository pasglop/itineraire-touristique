from array import array
from typing import List, Dict, Optional
from pydantic import BaseModel, Field, RootModel
from ..utils.db import connect_db

poi_detail_example = {
                "id": "678296",
                "name": "Tour Eiffel",
                "website": "https://www.toureiffel.paris/fr",
                "latitude": 48.85836,
                "longitude": 2.294543,
                "address": "Tour Eiffel\n5 avenue Anatole France\n75007 Paris",
                "phone": "+33 892 70 12 39",
                "description": "Symbole de la France dans le monde, la Tour Eiffel fut construite par Gustave Eiffel pour l’Exposition universelle de 1889, célébrant le centenaire de la Révolution française.",
                "classname": ['CulturalSite','RemarkableBuilding','Tower']
            }

class PoiDetailSchema(BaseModel):
    id: str
    name: str
    website: Optional[str]
    latitude: float
    longitude: float
    address: str
    phone: Optional[str]
    description: Optional[str]
    classname: List[str]
    class Config:
        json_schema_extra = {
            "example": poi_detail_example
        }

def get_poi_sql(where_clause: str, limit: int = None) -> str:
    query = f"""SELECT 
                    p.poi_id as id, p.name as name, 
                    p.website, p.latitude, p.longitude, 
                    p.name || '\n' || a.street || '\n' || a.zipcode || ' ' || a.locality as address,
                    co.phone, d.content as description, 
                   array_agg(c.type order by c.type) as classname 
                   FROM places p 
                   left join places_to_classes p2c using(poi_id)  
                   left JOIN public.classes c on p2c.classes_id = c.id 
                   left join addresses a using(poi_id)  
                   left join contacts co using(poi_id)  
                   left outer join public.descriptions d using(poi_id) 
                   WHERE {where_clause}
                   group by p.poi_id, p.name, p.website, p.latitude, p.longitude, a.street, a.zipcode, a.locality, co.phone, d.content
                   order by p.name"""
    if limit is not None:
        query += f" limit {limit}"
    return query

def get_poi_detail(poi_id: str) -> PoiDetailSchema | None:
    conn, cursor = connect_db()
    cursor.execute(get_poi_sql('p.poi_id = %s'), (poi_id,))

    poi = cursor.fetchone()

    if poi is None:
        return None

    return PoiDetailSchema(**poi)