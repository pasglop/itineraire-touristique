from source.data_processing.table_processing import TableProcessing, ProcessError


class PlacesToClassesProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "id": "dc_identifier",
            "places_id": "dc_identifier",
            "source_updated": "lastUpdateDatatourisme"
            "classes_id": "dc_identifier",
        }
        compare_keys = ["id"]
        super().__init__('public.places_to_classes', mapping, compare_keys, data, db_session)

    
    def process(self, data):
        # To make sure it is a valid entry, we need to check if it has places_id, classes_id fields
        if data['places_id'] is None or data['classes_id'] is None:
            raise ProcessError("One or more required fields are missing from the places_to_classes entry")
        super().process(data)
