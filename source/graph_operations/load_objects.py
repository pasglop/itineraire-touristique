from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import csv

from source.databases import connect_neo4j, disconnect_neo4j, connect_db, reset_graph, create_graph
from source.utils import get_project_root

load_dotenv()  # take environment variables from .env.


class LoadObjects:

    def __init__(self):
        self.db, self.cursor = connect_db()

    def load_data_from_db(self, limit=None):
        query = """
        SELECT p.id, p.name, 
        latitude, longitude, 
        a.street || '\n' || a.zipcode || ' ' || a.locality as address,
        array_agg(c.type) as class 
        FROM public.places p
        left join addresses a on p.id = a.places_id
        left join places_to_classes ptc on p.id = ptc.places_id
        left join classes c on ptc.classes_id = c.id 
        group by p.id, p.name, latitude, longitude, a.street, a.zipcode, a.locality
        """
        if limit is not None:
            query = query + " order by random() LIMIT " + str(limit)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def generate_csv_file_with_poi(self):
        # create file if not exists
        file_path = f"{get_project_root()}/neo4j/import/poi.csv"
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

    @staticmethod
    def copy_csv_file_to_neo4j():
        # copy csv file to neo4j import folder
        # get neo4j import folder from .env
        neo4j_import_folder = f"{get_project_root()}/neo4j/import/"
        file_path = f"{get_project_root()}/artifacts/*.csv"
        os.system(f"cp {file_path} {neo4j_import_folder}")
        return True

    @staticmethod
    def create_node_in_neo4j():
        # create node in neo4j from csv file
        # Cypher to import file
        query = '''LOAD CSV WITH HEADERS FROM 'file:///poi.csv' AS row CREATE (p:POI {id: row.id, name: row.name, 
        latitude: row.latitude, longitude: row.longitude, street: row.street, zipcode: row.zipcode, locality: 
        row.locality, class: row.class}) 
        SET p.coordinates = point({ latitude: toFloat(row.latitude), longitude: toFloat(
        row.longitude), height: 0 });'''
        reset_graph("POI")
        return create_graph(query)

    @staticmethod
    def load_stations():
        reset_graph("StationLine")
        query = '''
        LOAD CSV WITH HEADERS FROM 'file:///stations.csv' AS row
        CREATE (sl:StationLine {name: row.nom_clean + ' - ' + row.ligne, station:row.nom_gare, station_name: row.nom_clean, city:row.Ville, stats: toInteger(row.Trafic)})
        SET sl.coordinates = point({ latitude: toFloat(row.y), longitude: toFloat(row.x), height: 0 });
        '''

        summary = create_graph(query)
        print("Load_stations : created {nodes_created} nodes in {time} ms.".format(
            nodes_created=summary.counters.nodes_created,
            time=summary.result_available_after
        ))

        return summary

    @staticmethod
    def create_stations():
        reset_graph("Station")
        query = '''
        MATCH (sl1:StationLine)
        MERGE (s1:Station {name: sl1.station_name, station: sl1.station, city: sl1.city, stats: sl1.stats, coordinates: sl1.coordinates})
        MERGE (s1)-[:HAS_LINE {duration:0}]->(sl1)
        MERGE (sl1)-[:HAS_LINE {duration:0}]->(s1)
        '''
        summary = create_graph(query)
        print(
            "Load_stations : created {nodes_created} nodes and {relationships_created} relationships in {time} ms.".format(
                nodes_created=summary.counters.nodes_created,
                relationships_created=summary.counters.relationships_created,
                time=summary.result_available_after
            ))

        return summary

    @staticmethod
    def create_direct_correspondance():
        query = '''
        MATCH (sl1:StationLine)<-[:HAS_LINE]-(s1:Station)-[:HAS_LINE]->(sl2:StationLine)
        MERGE (sl1)-[r:DIRECT_CORRESPONDANCE {duration:240}]->(sl2) // 240s = 4mn
        MERGE (sl2)-[r2:DIRECT_CORRESPONDANCE {duration:240}]->(sl1)
        '''
        summary = create_graph(query)
        print("Create_direct_correspondance : created {relationships_created} relationships in {time} ms.".format(
            relationships_created=summary.counters.relationships_created,
            time=summary.result_available_after
        ))

        return summary

    @staticmethod
    def create_walk_correspondance():
        query = '''
        MATCH (s1:Station), (s2:Station)
        WHERE s1 <> s2 AND distance(s1.coordinates, s2.coordinates) <= 1000
        MERGE (s1)-[r:WALKING_CORRESPONDANCE]->(s2)
        SET r.distance = distance(s1.coordinates, s2.coordinates), 
        r.duration = distance(s1.coordinates, s2.coordinates) / 1.11111 // 1.11111 m/s for 4 km/h
        MERGE (s2)-[r2:WALKING_CORRESPONDANCE]->(s1)
        SET r2.distance = distance(s1.coordinates, s2.coordinates), 
        r2.duration = distance(s1.coordinates, s2.coordinates) / 1.11111
        '''
        summary = create_graph(query)
        print("Create_walk_correspondance : created {relationships_created} relationships in {time} ms.".format(
            relationships_created=summary.counters.relationships_created,
            time=summary.result_available_after
        ))

        return summary

    @staticmethod
    def create_lines():
        query = '''
        LOAD CSV WITH HEADERS FROM 'file:///liaisons.csv' AS row
        MATCH (sl1:StationLine {name: row.start + ' - ' + row.ligne}),
         (sl2:StationLine {name: row.stop + ' - ' + row.ligne})
        MERGE (sl1)-[r:IS_LINE {ligne: row.ligne}]->(sl2)
        SET r.distance = distance(sl1.coordinates, sl2.coordinates), r.duration = distance(sl1.coordinates, sl2.coordinates) / 11.11111111111111 // 11.11111111111111 m/s for 40 km/h
        MERGE (sl2)-[r2:IS_LINE {ligne: row.ligne}]->(sl1)
        SET r2.distance = distance(sl1.coordinates, sl2.coordinates), r2.duration = distance(sl1.coordinates, sl2.coordinates) / 11.11111111111111
        '''
        summary = create_graph(query)
        print("Create_lines : created {relationships_created} relationships in {time} ms.".format(
            relationships_created=summary.counters.relationships_created,
            time=summary.result_available_after
        ))

        return summary


if __name__ == "__main__":
    pass
