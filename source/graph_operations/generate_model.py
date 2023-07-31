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


def create_poi_relationships():
    # create a new label RemarkablePOI
    # create a new index on RemarkablePO
    query = '''
    CALL apoc.periodic.iterate("MATCH (n1:MustSeen)
    RETURN n1", "
    WITH n1
    MATCH (n2:MustSeen)
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


def get_shortest_path(df):
    gds = connect_gds()
    # first we need to project the graph for the community
    # then we need to run the shortest path algorithm
    # then we need to return the result


    try:
        gds.graph.drop(gds.graph.get('com_graph_0'))
    except:
        pass

    # project the graph
    all_com = df['nodeId'].tolist()
    all_com.append(5737)
    result = query_graph(f"""
    MATCH (source) WHERE ID(source) IN {df['nodeId'].tolist()} OR source:Station or source:StationLine
    MATCH (source)-[r]-(target)
    WHERE ID(target) IN {df['nodeId'].tolist()} OR target:Station or target:StationLine 
    WITH gds.graph.project(
          'com_graph_0',
          source,
          target,
          {{
                relationshipProperties: {{
                    cost: r.duration
                }}
            }}
        ) AS g
        RETURN g.graphName AS graph, g.nodeCount AS nodes, g.relationshipCount AS rels
    """)

    # run the shortest path algorithm
    result = query_graph(
        """
        CALL gds.beta.graph.relationships.stream(
  'com_graph_0'                  
)
YIELD
  sourceNodeId, targetNodeId, relationshipType
RETURN
  gds.util.asNode(sourceNodeId).name as source, gds.util.asNode(targetNodeId).name as target, relationshipType
ORDER BY source ASC, target ASC
        """
    )

    f"""
        CALL gds.alpha.allShortestPaths.stream('com_graph_0', {{
            relationshipWeightProperty: 'cost'
        }})
        YIELD sourceNodeId, targetNodeId, distance
        WITH sourceNodeId, targetNodeId, distance
        WHERE gds.util.isFinite(distance) = true
        MATCH (source:POI) WHERE id(source) = sourceNodeId
        MATCH (target:POI) WHERE id(target) = targetNodeId
        WITH source, target, distance WHERE source <> target and ID(source) = 5737
        RETURN source.name AS source, target.name AS target, distance as distance_in_kms

        """

    # return the result
    print(result)



    return result


def get_nodes_by_ids(node_ids):
    query = (
        f"MATCH (n:POI) WHERE ID(n) IN {node_ids} "
        "RETURN ID(n) as nodeId, n.mustseen as mustseen, n.remarkable as remarkable"
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
