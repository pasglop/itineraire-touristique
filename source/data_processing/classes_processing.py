from source.data_processing.table_processing import TableProcessing, ProcessError


class ClassesProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "id": "dc_identifier",
            "name": "isOwnedBy/0/schema_legalName",
            "type": "isOwnedBy/0/@type/1",
            "schema_url": "hasContact/0/foaf_homepage/0"
        }
        compare_keys = ["id"]
        super().__init__('public.classes', mapping, compare_keys, data, db_session)

    def process(self, data):
        # To make sure it is a valid entry, we need to check if it has dc_identifier field
        if data['dc_identifier'] is None:
            raise ProcessError("Field dc_identifier is missing from the classes entry")
        super().process(data)