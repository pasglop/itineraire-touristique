import pytest
from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from source.api.app.v1.poi import PoiDetailSchema, poi_detail_example
from source.databases import connect_db

class TestPoi:
    def test_should_return_true(self):
        assert True

    def test_should_generate_json_schema(self):
        # generate pydantic schema
        # and compare it with the expected schema
        model = PoiDetailSchema(**poi_detail_example).model_json_schema()
        assert model == {'$defs': {'PoiClass': {'properties': {'id': {'title': 'Id', 'type': 'integer'},
                                       'name': {'title': 'Name',
                                                'type': 'string'},
                                       'type': {'title': 'Type',
                                                'type': 'string'}},
                        'required': ['id', 'name', 'type'],
                        'title': 'PoiClass',
                        'type': 'object'},
                'PoiClassList': {'items': {'$ref': '#/$defs/PoiClass'},
                            'title': 'PoiClassList',
                            'type': 'array'}},
                'properties': {'address': {'title': 'Address', 'type': 'string'},
                'classname': {'$ref': '#/$defs/PoiClassList'},
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
                              'description',
                              'classname'],
                 'title': 'PoiDetailSchema',
                 'type': 'object'}

    def test_should_connect_db(self):
        conn, cursor = connect_db()
        assert db is not None

    def test_should_return_poi(self):
        assert False


if __name__ == '__main__':
    pytest.main()
