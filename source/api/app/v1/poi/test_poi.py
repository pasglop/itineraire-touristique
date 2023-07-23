import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from source.api.app import connect_db, app
from source.api.app.v1.poi import InputPoiClass, get_poi_by_class, get_poi_detail, PoiDetailSchema, poi_detail_example

parsedPoiDetailModel = {'properties': {'address': {'title': 'Address', 'type': 'string'},
                                       'classname': {'items': {'type': 'string'},
                                                     'title': 'Classname',
                                                     'type': 'array'},
                                       'description': {'title': 'Description', 'type': 'string'},
                                       'id': {'title': 'Id', 'type': 'integer'},
                                       'latitude': {'title': 'Latitude', 'type': 'number'},
                                       'longitude': {'title': 'Longitude', 'type': 'number'},
                                       'name': {'title': 'Name', 'type': 'string'},
                                       'phone': {'anyOf': [{'type': 'string'}, {'type': 'null'}],
                                                 'title': 'Phone'},
                                       'website': {'anyOf': [{'type': 'string'}, {'type': 'null'}],
                                                   'title': 'Website'}},
                        'required': ['id',
                                     'name',
                                     'website',
                                     'latitude',
                                     'longitude',
                                     'address',
                                     'phone',
                                     'description',
                                     'classname'],
                        'title': 'PoiDetailSchema',
                        'type': 'object'}


class TestPoi:
    def test_should_return_true(self):
        assert True

    def test_should_generate_json_schema(self):
        # generate pydantic schema
        # and compare it with the expected schema
        model = PoiDetailSchema(**poi_detail_example).model_json_schema()
        assert model == parsedPoiDetailModel

    def test_should_connect_db(self):
        conn, cursor = connect_db()
        assert conn is not None

    def test_should_return_poi_detail(self):
        assert get_poi_detail(678296).model_dump() == poi_detail_example

    def test_should_return_poi_through_api(self):
        # call api
        # compare result with expected result
        client = TestClient(app)
        response = client.get("/poi/678296")
        assert response.status_code == 200
        assert response.json() == poi_detail_example

    def test_should_return_poi_through_api_with_wrong_id(self):
        # call api
        # compare result with expected result
        client = TestClient(app)
        response = client.get("/poi/0")
        assert response.status_code == 404
        assert response.json() == {"detail": "Poi not found"}

    def test_should_return_poi_by_class(self):
        classes = InputPoiClass(classname='CulturalSite')
        result = get_poi_by_class(classes)
        assert result.poi[0].model_json_schema() == parsedPoiDetailModel

    def test_should_return_poi_by_class_through_api(self):
        # call api
        # compare result with expected result
        client = TestClient(app)
        response = client.get("/poi_by_class/CulturalSite")
        schema = response.json()['poi'][0]
        schema_test = PoiDetailSchema(**schema)
        assert response.status_code == 200
        assert schema_test.model_json_schema() == parsedPoiDetailModel

if __name__ == '__main__':
    pytest.main()
