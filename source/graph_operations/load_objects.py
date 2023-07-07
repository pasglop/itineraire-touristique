from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import csv

from source.databases import connect_neo4j, disconnect_neo4j, connect_db
from source.utils import get_project_root

load_dotenv()  # take environment variables from .env.


class LoadObjects:

    def __init__(self):
        self.graphdb = connect_neo4j()
        self.db, self.cursor = connect_db()

    def close(self):
        disconnect_neo4j(self.graphdb)

    def load_data_from_db(self, limit=None):
        query = """
        SELECT p.id, name, latitude, longitude, a.street, a.zipcode, a.locality 
        FROM public.places p 
        left join addresses a on p.id = a.places_id 
        """
        if limit is not None:
            query = query + " order by random() LIMIT " + str(limit)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def generate_csv_file_with_poi(self):
        # create file if not exists
        file_path = f"{get_project_root()}/raw_data/poi.csv"
        res = self.load_data_from_db()
        headers = [i[0] for i in self.cursor.description]
        csv_file = csv.writer(open(file_path, 'w'),
                              delimiter=',',
                              lineterminator='\r\n',
                              quoting=csv.QUOTE_ALL,
                              escapechar='\\')
        csv_file.writerow(headers)
        csv_file.writerows(res)
        return True


if __name__ == "__main__":
    pass
