import pytest
from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from api.app.v1.poi import PoiDetailSchema, poi_detail_example
class TestPoi:
    def test_should_return_true(self):
        assert True

    def test_should_generate_json_schema(self):
        # generate pydantic schema
        # and compare it with the expected schema
        model = PoiDetailSchema(**poi_detail_example).model_json_schema()
        assert model == {'properties': {'address': {'title': 'Address', 'type': 'string'},
                'description': {'title': 'Description', 'type': 'string'},
                'id': {'title': 'Id', 'type': 'integer'},
                'latitude': {'title': 'Latitude', 'type': 'number'},
                'longitude': {'title': 'Longitude', 'type': 'number'},
                'name': {'title': 'Name', 'type': 'string'},
                'phone': {'title': 'Phone', 'type': 'string'},
                'website': {'title': 'Website', 'type': 'string'}},
                 'required': ['id',
                              'name',
                              'website',
                              'latitude',
                              'longitude',
                              'address',
                              'phone',
                              'description'],
                 'title': 'PoiDetailSchema',
                 'type': 'object'}

    def test_should_connect_db(self):
        assert False

    def test_should_return_poi(self):
        assert False


if __name__ == '__main__':
    pytest.main()
