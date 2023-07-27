import psycopg2

from source.data_processing.table_processing import TableProcessing, ProcessError


class PlacesToClassesProcessing(TableProcessing):
    def __init__(self, data, db_session):
        mapping = {
            "poi_id": "dc_identifier",
            "classes_id": "@type"
        }
        compare_keys = ["poi_id"]
        super().__init__('public.places_to_classes', mapping, compare_keys, data, db_session)

    
    def process(self, data):
        # To make sure it is a valid entry, we need to check if it has places_id, classes_id fields
        if data['dc_identifier'] is None or data['@type'] is None:
            raise ProcessError("One or more required fields are missing from the places_to_classes entry")

        # this is a particular case as we have one place ID and many classes IDs
        # so we need to check all classes and place combinations
        for class_id in data['@type']:
            if ':' in class_id or 'PlaceOfInterest' in class_id or 'PointOfInterest' in class_id:
                continue
            super().process({
                'dc_identifier': data['dc_identifier'],
                '@type': class_id
            })

    def exists(self, where=None):
        """
        Special test as we use classes table to check if classes_id exists
        :param where:
        :param self:
        :return:
        """
        if where is None:
            try:
                where = self.prepare_comparison()
            except ProcessError:
                # bypass this record
                return True

        query = f"""
        SELECT 1 FROM public.places_to_classes p2c INNER JOIN public.classes c on p2c.classes_id = c.id
        WHERE {where} AND c.type = '{self.data['@type']}'
        """
        try:
            self.db_session.execute(query)
            result = self.db_session.fetchone()
        except psycopg2.Error as e:
            raise ProcessError(f"Error for record {self.data['dc_identifier']} : {e.pgerror}")

        if result is None:
            return False
        return True

    def insert(self):
        """
        Special insert as we use classes table to check if classes_id exists
        :param self:
        :return:
        """
        query = f"""
        INSERT INTO public.places_to_classes (poi_id, classes_id)
        VALUES (
        '{self.data['dc_identifier']}', 
        (select id from public.classes where type = '{self.data['@type']}')
        );
        """
        try:
            self.db_session.execute(query)
        except psycopg2.Error as e:
            raise ProcessError(f"Error for record {self.data['dc_identifier']} : {e.pgerror}")
        self.db_conn.commit()

    def update(self):
        """
        Special update as we use classes table to check if classes_id exists
        :param self:
        :return:
        """
        query = f"""
        UPDATE public.places_to_classes
        SET poi_id = '{self.data['dc_identifier']}',
            classes_id = (select id from public.classes where type = '{self.data['@type']}')
        WHERE {self.prepare_comparison()} AND 
        classes_id = (select id from public.classes where type = '{self.data['@type']}');
        """
        try:
            self.db_session.execute(query)
        except psycopg2.Error as e:
            raise ProcessError(f"Error for record {self.data['dc_identifier']} : {e.pgerror}")
        self.db_conn.commit()