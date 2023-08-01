from io import StringIO

import pandas as pd
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from source.databases import create_graph, connect_gds, reset_graph, query_graph

csv_remarkable = """
id, name, latitude, longitude
678296,Tour Eiffel,48.85836,2.294543
4679111,Cathédrale Notre-Dame de Paris,48.85267,2.349292
680785,Observatoire panoramique de la Tour Montparnasse,48.842162,2.322114
696760,Basilique du Sacré-Cœur de Montmartre,48.886704,2.343104
12dad4e8-8877-7077-b639-501ba37a0bee, Opéra national de Paris - Palais Garnier,48.871663,2.331864
682672,Arc de triomphe,48.873757,2.295909
705679,Centre Pompidou,48.860713,2.352254
705742,Galeries nationales du Grand Palais,48.8659,2.313395
700946,Musée du Louvre,48.861347,2.335457
776370,Parc des Buttes-Chaumont,48.876913,2.381105
697984,Petit Palais - Musée des Beaux Arts de la Ville de Paris,48.865895,2.313805
697946,Philharmonie de Paris - Cité de la musique,48.889306,2.393807
"""
poi_remarkable = pd.read_csv(StringIO(csv_remarkable), sep=",", dtype=str)


def drop_all_indexes():
    summary = create_graph("CALL apoc.schema.assert({},{},true) YIELD label, key RETURN * ")
    print("Dropping all indexes")
    return summary


def create_graph_index():
    create_graph("CREATE INDEX poi_id_index FOR (n:POI) ON (n.id)")
    summary = create_graph("CREATE INDEX coord_index FOR (n:POI) ON (n.coordinates)")
    print("Creation of index on POI(id) and POI(coordinates)")
    return summary


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
        gds.graph.drop(gds.graph.get('tmp_nodes'))
    except:
        pass

    g_tmp, res = gds.graph.project('tmp_nodes', node_config, relationship_config)

    print(
        f"Graph projected. {res.nodeCount} nodes and {res.relationshipCount} relationships projected in {res.projectMillis} ms.")

    return g_tmp, res

    # with gds.graph.project('tmp_nodes', node_config, relationship_config) as res:
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


def generate_kmeans_model(g_tmp, days=7):
    gds = connect_gds()
    km_result = gds.beta.kmeans.stream(
        g_tmp,
        nodeProperty="coord",
        relationshipTypes=["DISTANCE"],
        k=days,
        maxIterations=10,
        randomSeed=1235,
        computeSilhouette=True
    )

    node_ids = km_result['nodeId'].tolist()

    allnodes = pd.DataFrame(get_nodes_by_ids(node_ids))

    merged_df = pd.merge(km_result, allnodes, on='nodeId')
    merged_df['sort_order'] = merged_df.apply(sort_order, axis=1)
    sorted_df = (
        merged_df.sort_values(['communityId', 'sort_order'])
        .groupby('communityId')
        .head(8)
    )

    sorted_df = sorted_df.reset_index(drop=True)
    sorted_df = sorted_df.drop(columns=['sort_order'])
    return sorted_df

    # result = gds.graph.run(f"""
    # CALL gds.beta.kmeans.stream('mustseenodes', {{
    #             nodeProperty: 'coord',
    #           k: 7,
    #           maxIterations: 10,
    #           seedCentroids: [[48.85836, 2.294543], [48.85267, 2.349292], [48.842162, 2.322114], [48.886704, 2.343104], [48.871663, 2.331864], [48.873757, 2.295909], [48.860713, 2.352254]]
    #         }})
    #         YIELD nodeId, communityId, distanceFromCentroid, createMillis, computeMillis, writeMillis
    #         RETURN gds.util.asNode(nodeId).id AS poi_id,
    #                gds.util.asNode(nodeId).name AS name,
    #                gds.util.asNode(nodeId).mustseen AS mustseen,
    #                gds.util.asNode(nodeId).remarkable AS remarkable,
    #                communityId as day,
    #         distanceFromCentroid as distance
    #         ORDER BY communityId,
    #         CASE
    #                 WHEN remarkable IS NOT NULL AND remarkable = true THEN 1
    #                 WHEN remarkable IS NOT NULL AND remarkable = false THEN 2
    #                 WHEN mustseen IS NOT NULL AND mustseen = true THEN 3
    #                 ELSE 4
    #             END ASC,
    #         distance DESC,
    #             name ASC
    #         """)


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
        gds.graph.drop(gds.graph.get('com_graph_0'))
    except:
        pass

    g_tmp, res = gds.graph.project('com_graph_0', node_config, relationship_config)

    print(
        f"Graph projected. {res.nodeCount} nodes and {res.relationshipCount} relationships projected in {res.projectMillis} ms.")

    return res

def get_shortest_path(df, hotel_poi, index):
    gds = connect_gds()

    # use the projected graph to find the shortest path
    query = f"""
    MATCH (source) WHERE source.id = "{hotel_poi}"
    CALL gds.allShortestPaths.dijkstra.stream('com_graph_0', {{
    sourceNode: source,
    relationshipWeightProperty: 'duration'
    }})
    YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs, path
    WITH targetNode, sourceNode, totalCost, nodeIds, costs, path
    where gds.util.asNode(targetNode).id in {df['poi_id'].tolist()}
    RETURN
    gds.util.asNode(sourceNode).name AS sourceNodeName,
    gds.util.asNode(targetNode).name AS targetNodeName,
    totalCost,
    [nodeId IN nodeIds | gds.util.asNode(nodeId).name] AS nodeNames,
    costs,
    nodes(path) as path
    order by totalCost asc
    limit 1
    """

    result = query_graph(query)

    return result


def get_nodes_by_ids(node_ids):
    query = (
        f"MATCH (n:POI) WHERE ID(n) IN {node_ids} "
        "RETURN ID(n) as nodeId, n.id as poi_id, n.mustseen as mustseen, n.remarkable as remarkable"
    )
    summary = query_graph(query)
    return summary

def get_nodes_by_poi_ids(poi_ids):
    query = (
        f"MATCH (n:POI) WHERE n.id IN {poi_ids} "
        "RETURN n"
    )
    summary = query_graph(query)
    return summary


def sort_order(row):
    if row['remarkable'] is not None:
        if row['remarkable'] is True:
            return 1
        else:
            if row['mustseen'] is True:
                return 2
            elif row['mustseen'] is False:
                return 3

    return 4


if __file__ == "__main__":
    drop_all_indexes()
    create_graph_index()
