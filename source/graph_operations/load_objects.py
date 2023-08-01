from dotenv import load_dotenv
import os
import csv

load_dotenv()  # take environment variables from .env.

from source.databases import connect_db, reset_graph, create_graph, connect_gds
from source.utils import get_project_root


class LoadObjects:

    def __init__(self):
        self.db, self.cursor = connect_db()

    def load_data_from_db(self, limit=None):
        query = """
        SELECT p.poi_id as id, p.name, 
        latitude, longitude, 
        a.street || '\n' || a.zipcode || ' ' || a.locality as address,
        locality,
        array_agg(c.type) as class 
        FROM public.places p
        left join addresses a using(poi_id)
        left join places_to_classes ptc using(poi_id)
        left join classes c on ptc.classes_id = c.id 
        where c.type in ('CulturalSite', 'SportsAndLeisurePlaces', 'NaturalSite', 'Restaurant', 'Shopping', 'EntertainmentAndEvent', 'ParkAndGarden', 'Museum','BistroOrWineBar', 'Church', 'ArtGalleryOrExhibitionGallery', 'RemarkableBuilding', 'Castle', 'NightClub', 'SightseeingBoat', 'ZooAnimalPark', 'Hotel')
        group by p.poi_id, p.name, latitude, longitude, a.street, a.zipcode, a.locality
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
        latitude: toFloat(row.latitude), longitude: toFloat(row.longitude), street: row.street, zipcode: row.zipcode, locality: 
        row.locality}) 
        SET p.coordinates = point({ latitude: toFloat(row.latitude), longitude: toFloat(row.longitude), height: 0 })
        SET p.model_coordinates = [ toFloat(row.latitude), toFloat(row.longitude)] 
        SET p.listOfClass = apoc.convert.fromJsonList(row.class);'''
        reset_graph()
        return create_graph(query)

    @staticmethod
    def load_stations():
        reset_graph("StationLine")
        query = '''
        LOAD CSV WITH HEADERS FROM 'file:///stations.csv' AS row
        CREATE (sl:StationLine {name: row.nom_clean + ' - ' + row.ligne, station:row.nom_gare, station_name: row.nom_clean, city:row.Ville, stats: toInteger(row.Trafic)})
        SET sl.coordinates = point({ latitude: toFloat(row.x), longitude: toFloat(row.y), height: 0 });
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
        WHERE s1 <> s2 AND point.distance(s1.coordinates, s2.coordinates) <= 400
        MERGE (s1)-[r:WALKING_CORRESPONDANCE]->(s2)
        SET r.distance = point.distance(s1.coordinates, s2.coordinates), 
        r.duration = point.distance(s1.coordinates, s2.coordinates) / 1.11111 // 1.11111 m/s for 4 km/h
        MERGE (s2)-[r2:WALKING_CORRESPONDANCE]->(s1)
        SET r2.distance = point.distance(s2.coordinates, s1.coordinates), 
        r2.duration = point.distance(s2.coordinates, s1.coordinates) / 1.11111
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
        SET r.distance = point.distance(sl1.coordinates, sl2.coordinates), r.duration = point.distance(sl1.coordinates, sl2.coordinates) / 11.11111111111111 // 11.11111111111111 m/s for 40 km/h
        MERGE (sl2)-[r2:IS_LINE {ligne: row.ligne}]->(sl1)
        SET r2.distance = point.distance(sl2.coordinates, sl1.coordinates), r2.duration = point.distance(sl2.coordinates, sl1.coordinates) / 11.11111111111111
        '''
        summary = create_graph(query)
        print("Create_lines : created {relationships_created} relationships in {time} ms.".format(
            relationships_created=summary.counters.relationships_created,
            time=summary.result_available_after
        ))

        return summary

    @staticmethod
    def create_walk_to_station():
        query = '''
        MATCH (p:POI), (s:Station)
        WHERE id(p) <> id(s) AND point.distance(p.coordinates, s.coordinates) <= 800
        WITH p, s, point.distance(p.coordinates, s.coordinates) AS distance,
        point.distance(p.coordinates, s.coordinates) / 1.11111 AS duration
        MERGE (p)-[r:WALKING_TO_STATION]->(s)
        SET r.distance = distance, r.duration = duration 
        MERGE (s)-[r2:WALKING_FROM_STATION]->(p)
        SET r2.distance = distance, r2.duration = duration
        '''
        summary = create_graph(query)
        print("Create_walk_to_station : created {relationships_created} relationships in {time} ms.".format(
            relationships_created=summary.counters.relationships_created,
            time=summary.result_available_after
        ))

        return summary

    @staticmethod
    def drop_all_indexes():
        summary = create_graph("CALL apoc.schema.assert({},{},true) YIELD label, key RETURN * ")
        print("Dropping all indexes")
        return summary

    @staticmethod
    def create_graph_index():
        create_graph("CREATE INDEX poi_id_index FOR (n:POI) ON (n.id)")
        summary = create_graph("CREATE INDEX coord_index FOR (n:POI) ON (n.coordinates)")
        print("Creation of index on POI(id) and POI(coordinates)")
        return summary

    @staticmethod
    def extend_remarkable_pois():
        # create a new label RemarkablePOI
        # create a new index on RemarkablePO

        query = """
        LOAD CSV WITH HEADERS FROM 'file:///mustseen.csv' AS row
        MATCH (poi:POI {id: row.id})
        SET poi.mustseen = true
        SET poi.remarkable = CASE WHEN row.remarkable = '1' THEN true ELSE false END
        """
        summary = create_graph(query)
        return summary

    @staticmethod
    def generate_mustseen_labels():
        query = """
        MATCH(p:POI)
        where p.locality = 'Paris' and
        ANY(category IN ['Museum', 'RemarkableBuilding'] WHERE category in p.listOfClass)
        SET p:MustSeen
        """
        summary = create_graph(query)
        print("generate_mustseen_labels : created {labels_added} labels in {time} ms.".format(
            labels_added=summary.counters.labels_added,
            time=summary.result_available_after
        ))
        return summary

    @staticmethod
    def generate_hotels_labels():
        reset_graph('Hotel')
        query = """
        MATCH(p:POI)
        where p.locality = 'Paris' and
        ANY(category IN ['Hotel', 'Accomodation'] WHERE category in p.listOfClass)
        SET p:Hotel
        """
        summary = create_graph(query)
        print("generate_hotels_labels : created {labels_added} labels in {time} ms.".format(
            labels_added=summary.counters.labels_added,
            time=summary.result_available_after
        ))
        return summary

    @staticmethod
    def create_poi_relationships():
        query = '''
        CALL apoc.periodic.iterate("MATCH (n1:POI)
        RETURN n1", "
        WITH n1
        MATCH (n2:POI)
        WHERE id(n1) <> id(n2)
        WITH n1, n2, point.distance(n1.coordinates,n2.coordinates) as dist, 
        point.distance(n1.coordinates,n2.coordinates) / 1.11111 as duration 
        ORDER BY dist LIMIT 1
        CREATE (n1)-[r:DISTANCE{distance:dist, duration: duration}]->(n2)
        CREATE (n2)-[r2:DISTANCE{distance:dist, duration: duration}]->(n1)", {batchSize:1, parallel:true, concurrency:10})
        '''
        summary = create_graph(query)
        print("create_poi_relationships : created {relationships_created} relationships in {time} ms.".format(
            relationships_created=summary.counters.relationships_created,
            time=summary.result_available_after
        ))
        return summary

    @staticmethod
    def project_gds_model():
        gds = connect_gds()
        node_config = {
            "MustSeen": {
                "properties": {
                    "coord": {
                        'property': 'model_coordinates'
                    }
                }
            }
        }
        relationship_config = {
            "DISTANCE": {
                "properties": {
                    "distance": {
                        'property': 'distance'
                    }
                }
            }
        }

        try:
            gds.graph.drop(gds.graph.get('knn_graph'))
        except:
            pass

        g_tmp, res = gds.graph.project('knn_graph', node_config, relationship_config)

        print(
            f"Graph projected. {res.nodeCount} nodes and {res.relationshipCount} relationships projected in {res.projectMillis} ms.")

        return res

        # with gds.graph.project('knn_graph', node_config, relationship_config) as res:
        #     g_tmp, project_result = res
        #
        #     print(g_tmp)
        #     print(project_result)
        #     km_result = gds.kmeans.stream(g_tmp, {
        #         "nodeProperties": ["coord"],
        #         "k": 7,
        #         "maxIterations": 10
        #     })
        #     print(km_result)

    @staticmethod
    def project_gds_model_mustseen_and_hotels():
        gds = connect_gds()
        node_config = {
            "MustSeen": {
                "properties": ['latitude', 'longitude']
            },
            "Hotel": {
                "properties": ['latitude', 'longitude']
            },
            "Station": {
                "properties": ['latitude', 'longitude']
            },
            "StationLine": {}
        }
        relationship_config = {
            "DISTANCE": {
                "properties": ['distance', 'duration']
            },
            "IS_LINE": {
                "properties": ['distance', 'duration']
            },
            "HAS_LINE": {
                "properties": ['distance', 'duration']
            },
            "WALKING_TO_STATION": {
                "properties": ['distance', 'duration']
            },
            "WALKING_FROM_STATION": {
                "properties": ['distance', 'duration']
            },
            "WALKING_CORRESPONDANCE": {
                "properties": ['distance', 'duration']
            },
            "DIRECT_CORRESPONDANCE": {
                "properties": ['distance', 'duration']
            }
        }

        try:
            gds.graph.drop(gds.graph.get('shortest_path_graph'))
        except:
            pass

        g_tmp, res = gds.graph.project('shortest_path_graph', node_config, relationship_config)

        print(
            f"Graph projected. {res.nodeCount} nodes and {res.relationshipCount} relationships projected in {res.projectMillis} ms.")

        return res


if __name__ == "__main__":
    pass
