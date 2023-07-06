from source.data_processing.table_processing import TableProcessing, ProcessError


class ClassesProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "id": "dc_identifier",
            "name": "label",
            "type": "type",
            "schema_url": "schema_url"
        }
        compare_keys = ["id"]
        super().__init__('public.classes', mapping, compare_keys, data, db_session)

    def find_object(self):
        """
        This function is used to find the object in the database and check if it needs to be updated.
        :return: boolean
        """
        return self.exists(f"id = '{self.data['dc_identifier']}'")

    def process(self, data):
        # To make sure it is a valid entry, we need to check if it has dc_identifier field
        if data['dc_identifier'] is None:
            raise ProcessError("Field dc_identifier is missing from the classes entry")
        super().process(data)