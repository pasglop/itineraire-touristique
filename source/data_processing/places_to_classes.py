from source.data_processing.table_processing import TableProcessing, ProcessError


class PlacesToClassesProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "id": "dc_identifier",
            "places_id": "places_id",
            "createAt": "createAt",
            "updateAt": "updateAt",
            "classes_id": "classes_id"
        }
        compare_keys = ["id"]
        super().__init__('public.places_to_classes', mapping, compare_keys, data, db_session)

    def find_object(self):
        """
        This function is used to find the object in the database and check if it needs to be updated.
        :return: boolean
        """
        return self.exists(f"places_id = '{self.data['places_id']}' AND classes_id = '{self.data['classes_id']}'")

    def process(self, data):
        # To make sure it is a valid entry, we need to check if it has places_id, classes_id fields
        if data['places_id'] is None or data['classes_id'] is None:
            raise ProcessError("One or more required fields are missing from the places_to_classes entry")
        super().process(data)
