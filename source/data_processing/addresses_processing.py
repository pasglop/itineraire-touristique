from source.data_processing.table_processing import TableProcessing, ProcessError


class AddressesProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "places_id": "dc_identifier",
            "schema_url": 'isLocatedAt/0/schema_address/@id',
            "locality": 'isLocatedAt/0/schema_address/schema_addressLocality',
            "zipcode": 'isLocatedAt/0/schema_address/schema_postalCode',
            "street": 'isLocatedAt/0/schema_address/0/schema_streetAddress',
            "source_updated": "lastUpdateDatatourisme"
        }
        compare_keys = ["places_id", "source_updated"]
        super().__init__('addresses', mapping, compare_keys, data, db_session)


    def process(self, data):
        # To make sure it is a POI, we need to check dc_identifier
        if data['dc_identifier'] is None:
            raise ProcessError(f"Field dc_identifier is missing from the object")
        super().process(data)
