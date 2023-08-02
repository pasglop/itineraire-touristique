from typing import List, Union

import pandas as pd
import haversine as hs
import logging
from io import StringIO

from pydantic import ValidationError

from .itinary_models import ItinaryCreationSchema, ItinarySchema, ItinaryCreationResponseSchema, WalkDetailSchema, \
    SubwayDetailSchema, VisitDetailSchema, ItinarySchemaDays, ItinaryStepGenericSchema, ItinaryStepWalkSchema, \
    ItinaryStepSubwaySchema, ItinaryStepVisitSchema, ItinaryStepEatSchema
from ..poi import PoiDetailSchema, get_poi_detail
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
        result = self.generate_itinary(payload.days, payload.hotel_poi)
        itinary_id = self._save_itinary()

        return ItinaryCreationResponseSchema(itinary_id=itinary_id, itinary=result)

    def _save_itinary(self):
        # private method
        # save the itinary in the db TODO
        return 1234

    def _create_knn_model(self, days: int = 7, hotel_poi_id: str = None):
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
        self.days_df = {community_id: df for community_id, df in sorted_df.groupby('communityId')}
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

    def _find_next_step(self, list_poi: list, poi_id: str):

        # get the shortest path POI walking or taking the subway
        query = f"""
            MATCH (source) WHERE source.id = "{poi_id}"
            CALL gds.allShortestPaths.dijkstra.stream('shortest_path_graph', {{
            sourceNode: source,
            relationshipWeightProperty: 'duration'
            }})
            YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs, path
            WITH targetNode, sourceNode, totalCost, nodeIds, costs, path
            where gds.util.asNode(targetNode).id in {list_poi}
            RETURN
            gds.util.asNode(sourceNode).name AS sourceNodeName,
            gds.util.asNode(sourceNode).id AS sourceNodePoiId,
            gds.util.asNode(targetNode).name AS targetNodeName,
            gds.util.asNode(targetNode).id AS targetNodePoiId,
            totalCost,
            [nodeId IN nodeIds | gds.util.asNode(nodeId).name] AS nodeNames,
            [nodeId IN nodeIds | labels(gds.util.asNode(nodeId))] AS nodeLabels,
            costs,
            nodes(path) as path
            order by totalCost asc
            limit 1
            """
        result = None
        try:
            result = query_graph(query)[0]
        except Exception as e:
            print(e, query)

        return result

    def _add_to_steps(self, day_index, step):
        # private method
        # add the step to the list of steps
        self.list_steps[day_index]['steps'].append(step)
        return True

    def _init_steps(self):
        # private method
        # create as much days as needed
        self.list_steps = [{'Day': x + 1, 'day_index': x, 'steps': []} for x in self.days_df.keys()]
        return True

    def _compute_itinary(self, days: int, hotel_poi_id: str):
        # private method

        # init the steps
        self._init_steps()

        # for each day from range 0 to days
        poi_id = None
        for day_index in range(0, days):
            # get list of POIs
            df_pois = self.days_df[day_index]
            nb_steps = len(df_pois)

            step = None
            for step_index in range(0, nb_steps):
                if step_index == 0:
                    # generate the first step from the hotel to the first POI
                    step = self._find_next_step(list_poi=df_pois['poi_id'].tolist(), poi_id=hotel_poi_id)
                    self._add_to_steps(day_index=day_index, step=step)
                    logging.info(f"Day {day_index + 1} - start - {step['sourceNodeName']} -> {step['targetNodeName']}")

                # find the target poi in step
                poi_id = step['targetNodePoiId']
                # remove the target poi from the list of pois
                df_pois = df_pois[df_pois['poi_id'] != poi_id]

                if len(df_pois) > 0:
                    # generate the next step
                    step = self._find_next_step(df_pois['poi_id'].tolist(), poi_id=poi_id)
                    self._add_to_steps(day_index=day_index, step=step)
                    logging.info(
                        f"Day {day_index + 1} - {step_index} - {step['sourceNodeName']} -> {step['targetNodeName']}")

            # generate the last step
            step = self._find_next_step(list_poi=[hotel_poi_id], poi_id=poi_id)
            self._add_to_steps(day_index=day_index, step=step)
            logging.info(f"Day {day_index + 1} - Final - {step['sourceNodeName']} -> {step['targetNodeName']}")

    def _map_to_walk(self, current_step, next_step) -> WalkDetailSchema:
        result = None
        loc1 = (current_step.get('latitude'), current_step.get('longitude'))
        loc2 = (current_step.get('latitude'), current_step.get('longitude'))
        distance = hs.haversine(loc1, loc2)
        duration = next_step.get('cost') - current_step.get('cost')
        return WalkDetailSchema(
            name=f'Marcher de {"la station " + current_step["station"] if "Station" in current_step["labels"]  else current_step["name"]} à {"la station" + next_step["station"] if "Station" in next_step["labels"] else next_step["name"]} pendant {duration} minutes',
            distance=distance,  # compute this from lat/lon if available
            duration=duration,
            start_latitude=current_step.get('latitude'),
            start_longitude=current_step.get('longitude'),
            end_latitude=next_step.get('latitude'),
            end_longitude=next_step.get('longitude'),
        )

    def _map_to_subway(self, all_steps, previous_step) -> SubwayDetailSchema:
        current_step = all_steps[0]
        next_step = all_steps[1]
        future_steps = all_steps[1:]
        line = next_step['name'].split(' - ')[1]
        nb_stations = 1
        msg = ''
        duration = 0
        final_station = None
        dir = 'toto' # TODO find the direction with neo4j

        j = 0
        while j < len(future_steps) and 'StationLine' in future_steps[j]['labels'][0]:
            j += 1
            nb_stations += 1
            final_station = future_steps[j]['name']
            duration = future_steps[j]['cost'] - current_step['cost']

        if previous_step['labels'][0] == 'StationLine':
            # Correspondance entre deux lignes
            prev_line = previous_step['name'].split(' - ')[1]
            msg = f'A la station {current_step["station"]}, prenez la correspondance entre la ligne {prev_line} et la ligne {line} en direction de {dir} jusqu\'à {final_station}'
        else:
            # prendre le métro jusqu'à la prochaine station
            msg = f'Prendre le métro ligne {line} en direction de {dir} jusqu\'à {final_station}'

        return SubwayDetailSchema(
            name=msg,
            duration=duration,
            line=line,
            direction=dir,
            nb_stations=nb_stations,
            final_station=final_station
        )

    def _map_to_visit(self, step_detail) -> VisitDetailSchema:
        poi_detail = get_poi_detail(step_detail['id'])

        return VisitDetailSchema(**poi_detail.model_dump())

    def _combine_paths(self, paths: List[dict], costs: List[float], labels: List[List[str]]) -> List[dict]:
        # private method
        # combine the paths to a single path
        path_combined = []

        for dict_elem, cost_elem, labels_elem in zip(paths, costs, labels):
            dict_elem['cost'] = cost_elem
            dict_elem['labels'] = labels_elem
            path_combined.append(dict_elem)

        return path_combined

    def _map_step(self, step_path: dict) -> list[ItinaryStepWalkSchema | ItinaryStepSubwaySchema | ItinaryStepEatSchema | ItinaryStepVisitSchema]:
        # private method
        # map the step to a dict ready for step_details
        results = []
        path = self._combine_paths(step_path['path'], step_path['costs'], step_path['nodeLabels'])

        for i in range(len(path) - 1):
            result = None
            label = path[i]['labels']
            if 'POI' in label or ('Station' in label and 'POI' in path[i+1]['labels']):
                stepdetail = self._map_to_walk(path[i], path[i+1])
                result = ItinaryStepWalkSchema(step=(i+1), name=path[i]['name'], step_detail=stepdetail.model_dump(), instruction=' ')
            elif 'Station' in label:
                stepdetail = self._map_to_subway(path[i:], path[i-1])
                result = ItinaryStepSubwaySchema(step=(i+1), name=path[i]['name'], step_detail=stepdetail.model_dump(), instruction=' ')
            elif 'MustSeen' in label:
                stepdetail = self._map_to_visit(path[i])
                result = ItinaryStepVisitSchema(step=(i+1), name=path[i]['name'], step_detail=stepdetail.model_dump(), instruction=' ')
            else:
                continue
            results.append(result)
        return results

    def generate_itinary(self, nb_days: int, hotel_poi_id: str) -> ItinarySchemaDays:
        # generate the itinary

        # first generate knn_model
        self._create_knn_model(nb_days, hotel_poi_id)

        # run the itinary generation
        self._compute_itinary(nb_days, hotel_poi_id)

        # return a list of itinary
        itinary = []
        for day_index in range(nb_days):
            steps = self.list_steps[day_index]['steps']
            itinary_steps = []

            for step in steps:
                try:
                    step_detail = self._map_step(step)
                    itinary_steps += step_detail
                except ValidationError as e:
                    logging.error(e)
                    raise e

            # Create a single ItinarySchema instance with all the steps
            itinary_day = ItinarySchema(steps=itinary_steps)
            itinary.append(itinary_day)
        return ItinarySchemaDays(days=itinary)
