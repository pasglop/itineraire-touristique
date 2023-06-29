from source.data_processing.table_processing import TableProcessing, ProcessError


class DescriptionsProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "places_id": "dc_identifier",
            "lang": 'hasDescription/0/shortDescription/fr',
            "schema_url": 'hasDescription/@id',
            "source_updated": "lastUpdateDatatourisme"
        }
        compare_keys = ["places_id", "source_updated"]
        super().__init__('descriptions', mapping, compare_keys, data, db_session)


    def process(self, data):
        # To make sure it is a POI, we need to check dc_identifier
        if data['dc_identifier'] is None:
            raise ProcessError(f"Field dc_identifier is missing from the object")
        super().process(data)    