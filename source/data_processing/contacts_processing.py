from source.data_processing.table_processing import TableProcessing, ProcessError


class ContactsProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "id": "dc_identifier",
            "places_id": "places_id",
            "from": "opens",
            "trough": "closes"
        }
        compare_keys = ["id"]
        super().__init__('public.contacts', mapping, compare_keys, data, db_session)

    def find_object(self):
        """
        This function is used to find the object in the database and check if it needs to be updated.
        :return: boolean
        """
        return self.exists(f"places_id = '{self.data['places_id']}' AND opens = '{self.data['opens']}' AND closes = '{self.data['closes']}'")

    def process(self, data):
        # To make sure it is a valid contact entry, we need to check if it has places_id, opens, and closes fields
        if data['places_id'] is None or data['opens'] is None or data['closes'] is None:
            raise ProcessError("One or more required fields are missing from the contact entry")
        super().process(data)