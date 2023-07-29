from io import StringIO

import pandas
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from source.databases import create_graph, connect_gds, reset_graph

csv_remarkable = """
id, name, latitude, longitude
678296,Tour Eiffel,48.85836,2.294543
682672,Arc de triomphe,48.873757,2.295909
4679111,Cathédrale Notre-Dame de Paris,48.85267,2.349292
696760, Basilique du Sacré-Cœur de Montmartre,48.886704,2.343104
705679,Centre Pompidou,48.860713,2.352254
705742,Galeries nationales du Grand Palais,48.8659,2.313395
700946,Musée du Louvre,48.861347,2.335457
680785,Observatoire panoramique de la Tour Montparnasse,48.842162,2.322114
696931,Palais Garnier,48.871663,2.331864
776370,Parc des Buttes-Chaumont,48.876913,2.381105
697984,Petit Palais - Musée des Beaux Arts de la Ville de Paris,48.865895,2.313805
697946,Philharmonie de Paris - Cité de la musique,48.889306,2.393807
"""
poi_remarkable = pandas.read_csv(StringIO(csv_remarkable), sep=",", dtype=str)


def drop_all_indexes():
    summary = create_graph("CALL apoc.schema.assert({},{},true) YIELD label, key RETURN * ")
    print("Dropping all indexes")
    return summary


def create_graph_index():
    create_graph("CREATE INDEX ON :POI(id)")
    summary = create_graph("CREATE INDEX ON :POI(coordinates)")
    print("Creation of index on POI(id) and POI(coordinates)")
    return summary


def extend_remarkable_pois():
    # create a new label RemarkablePOI
    # create a new index on RemarkablePO
    query = """
    LOAD CSV WITH HEADERS FROM 'file:///mustseen.csv' AS row
    MATCH (poi:POI {id: row.id})
    SET poi.mustseen = true
    """
    summary = create_graph(query)
    return summary


def create_poi_relationships():
    # create a new label RemarkablePOI
    # create a new index on RemarkablePO
    query = '''
    CALL apoc.periodic.iterate("MATCH (n1:POI)
    RETURN n1", "
    WITH n1
    MATCH (n2:POI)
    WHERE id(n1) <> id(n2)
    WITH n1, n2, distance(n1.coordinates,n2.coordinates) as dist, 
    distance(n1.coordinates,n2.coordinates) / 1.11111 as duration 
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


def generate_mustseen_labels():
    reset_graph('MustSeen')
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


def project_gds_model():
    gds = connect_gds()
    gds.graph.drop('mustseenodes')
    result = gds.graph.project('mustseenodes',
                                         {
                                             "MustSeen": {
                                                 "properties": {
                                                     "id": {
                                                         "property": 'id'
                                                     },
                                                     "coord": {
                                                         property: 'model_coordinates'
                                                     }
                                                 }
                                             }
                                         }
                                         )
    print("project_gds_model : created {nodes_count} nodes in {time} ms.".format(
        nodes_count=result.nodes_created,
        time=result.result_available_after
    ))
    return result

def generate_kmeans_model():
    gds = connect_gds()
    result = gds.graph.run("CALL gds.beta.kmeans.write('mustseenodes', {"
                           "writeProperty: 'kmeans', "
                           "maxIterations: 10, "
                           "k: 5, "
                           "nodeWeightProperty: 'weight', "
                           "concurrency: 4, "
                           "writeConcurrency: 4, "
                           "embeddingDimension: 2, "
                           "embeddingWeightProperty: 'embedding', "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2, "
                           "embeddingFeatureProperty: 'embeddingFeature', "
                           "embeddingFeatureDimension: 2"
                           "}) YIELD nodesCommitted, relationshipsCommitted, createMillis, computeMillis, writeMillis")
    print("generate_kmeans_model : created {nodes_count} nodes and {relationships_count} relationships in {time} ms.".format(
        nodes_count=result.nodesCommitted,
        relationships_count=result.relationshipsCommitted,
        time=result.createMillis + result.computeMillis + result.writeMillis
    ))
    return result


if __file__ == "__main__":
    drop_all_indexes()
    create_graph_index()
