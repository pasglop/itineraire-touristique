from source.data_processing.table_processing import TableProcessing, ProcessError


class DescriptionsProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "poi_id": "dc_identifier",
            "content": 'hasDescription/0/shortDescription/fr/0',
            "schema_url": 'hasDescription/0/@id'
        }
        compare_keys = ["poi_id"]
        super().__init__('descriptions', mapping, compare_keys, data, db_session)


    def process(self, data):
        # To make sure it is a POI, we need to check dc_identifier
        if data['dc_identifier'] is None:
            raise ProcessError(f"Field dc_identifier is missing from the object")
        super().process(data)    