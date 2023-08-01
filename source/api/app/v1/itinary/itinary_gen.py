import pandas as pd
from io import StringIO

from .itinary_models import ItinaryCreationSchema, ItinarySchema, ItinaryCreationResponseSchema
from ..utils.db import connect_db
from ..utils.graph import connect_gds, query_graph


class ItinaryGenerator:
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

    def __init__(self):
        self.db, self.cursor = connect_db()
        self.knn_model = None
        self.days_df = None
        self.poi_remarkable = None
        self.list_steps = []

    def load_poi_remakable(self):
        self.poi_remarkable = pd.read_csv(StringIO(self.csv_remarkable), sep=",", dtype=str)

    def create_itinary(self, payload: ItinaryCreationSchema) -> ItinaryCreationResponseSchema:
        # public method
        # first create the KNN model
        self._create_knn_model(days=payload.days)

        # then generate each steps with path

        # Map to step classes

        # save the itinary
        itinary_id = self._save_itinary()

        return ItinaryCreationResponseSchema(itinary_id=itinary_id)

    def _save_itinary(self):
        # private method
        # save the itinary in the db
        return 1234

    def _create_knn_model(self, days: int = 7):
        # private method
        # create the knn model
        gds = connect_gds()
        g_knn = gds.graph.get("knn_graph")
        km_result = gds.beta.kmeans.stream(
            g_knn,
            nodeProperty="coord",
            relationshipTypes=["DISTANCE"],
            k=days,
            maxIterations=10,
            randomSeed=1235,
            computeSilhouette=True
        )

        node_ids = km_result['nodeId'].tolist()

        allnodes = pd.DataFrame(self.get_nodes_by_ids(node_ids))

        merged_df = pd.merge(km_result, allnodes, on='nodeId')
        merged_df['sort_order'] = merged_df.apply(self.sort_order, axis=1)
        sorted_df = (
            merged_df.sort_values(['communityId', 'sort_order'])
            .groupby('communityId')
            .head(8)
        )

        sorted_df = sorted_df.reset_index(drop=True)
        sorted_df = sorted_df.drop(columns=['sort_order'])

        days = sorted_df.groupby('communityId')
        self.days_df = {community_id: df for community_id, df in days}

        self.knn_model = sorted_df

        return True

    def sort_order(self, row):
        if row['remarkable'] is not None:
            if row['remarkable'] is True:
                return 1
            else:
                if row['mustseen'] is True:
                    return 2
                elif row['mustseen'] is False:
                    return 3

        return 4

    def get_nodes_by_ids(self, node_ids):
        query = (
            f"MATCH (n:POI) WHERE ID(n) IN {node_ids} "
            "RETURN ID(n) as nodeId, n.id as poi_id, n.mustseen as mustseen, n.remarkable as remarkable"
        )
        summary = query_graph(query)
        return summary

    def get_nodes_by_poi_ids(self, poi_ids):
        query = (
            f"MATCH (n:POI) WHERE n.id IN {poi_ids} "
            "RETURN n"
        )
        summary = query_graph(query)
        return summary


    def _find_next_step(self, day_index, start_node):
        daily_df = self.days_df[day_index]

        # get the shortest path POI walking or taking the subway
        query = f"""
            MATCH (source) WHERE source.id = "{start_node['n']['id']}"
            CALL gds.allShortestPaths.dijkstra.stream('shortest_path_graph', {{
            sourceNode: source,
            relationshipWeightProperty: 'duration'
            }})
            YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs, path
            WITH targetNode, sourceNode, totalCost, nodeIds, costs, path
            where gds.util.asNode(targetNode).id in {daily_df['poi_id'].tolist()}
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
        result = query_graph(query)[0]

        self.list_steps[day_index]['steps'].append(result)

        return result

    def _init_steps(self):
        # private method
        # create as much days as needed
        self.list_steps = [{'Day': x+1, 'day_index': x, 'steps': []} for x in self.days_df.keys()]
        return True



