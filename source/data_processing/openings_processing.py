from source.data_processing.table_processing import TableProcessing, ProcessError


class OpeningsProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "poi_id": "dc_identifier",
            "start_date": 'isLocatedAt/0/schema_openingHoursSpecification/0/schema_validFrom',
            "end_date": 'isLocatedAt/0/schema_openingHoursSpecification/0/schema_validThrough',
            "opens": 'isLocatedAt/0/schema_openingHoursSpecification/0/schema_opens', # valeur pas toujours disponible selon json
            "closes": 'isLocatedAt/0/schema_openingHoursSpecification/0/schema_closes'       
        }
        compare_keys = ["poi_id"]
        super().__init__('openings', mapping, compare_keys, data, db_session)
        

    def process(self, data):
        # To make sure it is a POI, we need to check dc_identifier
        if data['dc_identifier'] is None:
            raise ProcessError(f"Field dc_identifier is missing from the object")
        super().process(data)        