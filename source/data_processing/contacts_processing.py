from source.data_processing.table_processing import TableProcessing, ProcessError								
								
								
class ContactsProcessing(TableProcessing):								
    def __init__(self, data, db_session):								
        mapping = {								
            "places_id": "dc_identifier",								
            "schema_url": 'hasContact/0/foaf_homepage/0',								
            "type": 'hasContact/0/@type/1',								
            "phone": 'hasContact/0/schema_telephone/0',								
            "source_updated": "lastUpdateDatatourisme"								
            }								
        compare_keys = ["places_id", "source_updated"]								
        super().__init__('contacts', mapping, compare_keys, data, db_session)								
								
								
    def process(self, data):								
 # To make sure it is a POI, we need to check dc_identifier								
       if data['dc_identifier'] is None:								
        raise ProcessError(f"Field dc_identifier is missing from the object')
                          
