from source.data_processing.table_processing import TableProcessing, ProcessError


class AddressesProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "poi_id": "dc_identifier",
            "schema_url": 'isLocatedAt/0/schema_address/0/@id',
            "locality": 'isLocatedAt/0/schema_address/0/schema_addressLocality',
            "zipcode": 'isLocatedAt/0/schema_address/0/schema_postalCode',
            "street": 'isLocatedAt/0/schema_address/0/schema_streetAddress/0'
        }
        compare_keys = ["poi_id"]
        super().__init__('addresses', mapping, compare_keys, data, db_session)


    def process(self, data):
        # To make sure it is a POI, we need to check dc_identifier
        if data['dc_identifier'] is None:
            raise ProcessError(f"Field dc_identifier is missing from the object")
        super().process(data)
