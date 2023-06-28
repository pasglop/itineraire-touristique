from source.data_processing.table_processing import TableProcessing, ProcessError


class OpeningsProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "places_id": "dc_identifier",
            "from": 'isLocatedAt/0/schema_openingHoursSpecification/schema_validFrom',
            "through": 'isLocatedAt/0/schema_openingHoursSpecification/schema_validThrough',
            "opens": 'isLocatedAt/0/schema_openingHoursSpecification/schema_opens', # valeur pas toujours disponible selon json
            "closes": 'isLocatedAt/0/schema_openingHoursSpecification/schema_closes', # valeur pas toujours disponible selon json
            "source_updated": "lastUpdateDatatourisme"          
        }
        compare_keys = ["places_id", "source_updated"]
        super().__init__('openings', mapping, compare_keys, data, db_session)
        

    def process(self, data):
        # To make sure it is a POI, we need to check dc_identifier
        if data['dc_identifier'] is None:
            raise ProcessError(f"Field dc_identifier is missing from the object")
        super().process(data)        