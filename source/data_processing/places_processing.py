from source.data_processing.table_processing import TableProcessing, ProcessError


class PlacesProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "id": "dc_identifier",
            "name": "label",
            "schema_url": "schema_url",
            "website": 'hasContact/0/foaf_homepage/0',
            "latitude": 'isLocatedAt/0/schema_geo/schema_latitude',
            "longitude": 'isLocatedAt/0/schema_geo/schema_longitude',
            "source_updated": "lastUpdateDatatourisme"
        }
        compare_keys = ["id", "source_updated"]
        super().__init__('public.places', mapping, compare_keys, data, db_session)

    def find_object(self):
        """
        This function is used to find the object in the database.
        and check if it needs to be updated.
        :param json_obj: object from json TOC
        :param cur: DB cursor
        :return: boolean
        """
        return self.exists(
            f"schema_url = '{self.data['schema_url']}' AND source_updated <= '{self.data['lastUpdateDatatourisme']}'")

    def process(self, data):
        # To make sure it is a POI, we need to check dc_identifier
        if data['dc_identifier'] is None:
            raise ProcessError(f"Field dc_identifier is missing from the object")
        super().process(data)
