import pytest
from fastapi.testclient import TestClient

import dotenv

dotenv.load_dotenv()
from .app import app
from .v1.itinary.itinary_gen import ItinaryGenerator

from .v1.itinary.itinary_models import ItinaryStepVisitSchema, ItinaryStepWalkSchema, VisitDetailSchema, WalkDetailSchema
from .v1.poi import poi_detail_example


def test_itinary_step_visit_schema():
    poi = poi_detail_example
    step_detail = VisitDetailSchema(**poi)
    itinary_step = ItinaryStepVisitSchema(
        step=1,
        name=poi['name'],
        step_detail=step_detail,
        instruction='Visiter',
        comment='Commentaire'
    )
    assert itinary_step.step_type == 'Visiter'
    assert itinary_step.step_detail.name == 'Tour Eiffel'

def test_itinary_step_walk_schema():
    walk_detail = WalkDetailSchema(
        name='Marcher vers la tour Eiffel',
        distance=1000,
        duration=10,
        start_latitude=48.85836,
        start_longitude=2.294543,
        end_latitude=48.85836,
        end_longitude=2.294543
    )
    itinary_step = ItinaryStepWalkSchema(
        step=1,
        name='Marcher vers la tour Eiffel',
        step_detail=walk_detail,
        instruction='Marcher',
        comment='Commentaire'
    )
    assert itinary_step.step_type == 'Marcher'
    assert itinary_step.step_detail.duration == 10


def test_should_connect_db():
    igen = ItinaryGenerator()
    assert igen.db is not None

def test_should_post_itinary_parameters_and_get_an_itinary_id():
    client = TestClient(app)
    payload = {
        "hotel_poi": "id-poi-hotel",
        "days": 2,
    }
    response = client.post("/itinary", json=payload)
    assert response.status_code == 200
    assert response.json()['itinary_id'] is not None

def test_should_generate_knn_model():
    igen = ItinaryGenerator()
    igen._create_knn_model()
    assert igen.knn_model is not None


def test_generate_kmeans_model():
    """
    Test the kmeans model
    I want to have 7 communities (days) with at most 8 pois per community
    :return:
    """
    g_tmp, p = project_gds_model()
    assert p.nodeCount > 0 and p.relationshipCount > 0
    k = generate_kmeans_model()
    # Count the number of unique communities
    num_communities = k['communityId'].nunique()
    assert num_communities == 7

    # Count the number of rows for each community
    num_rows_per_community = k['communityId'].value_counts()
    assert num_rows_per_community.min() > 0 and num_rows_per_community.max() <= 8

def test_generate_kmeans_model_with_2_communities():
    """
    Test the kmeans model
    I want to have 2 communities (days) with at most 8 pois per community
    :return:
    """
    g_tmp, p = project_gds_model()
    assert p.nodeCount > 0 and p.relationshipCount > 0
    k = generate_kmeans_model(g_tmp, days=2)

    print(k)
    # Count the number of unique communities
    num_communities = k['communityId'].nunique()
    assert num_communities == 2

    # Count the number of rows for each community
    num_rows_per_community = k['communityId'].value_counts()
    assert num_rows_per_community.min() > 0 and num_rows_per_community.max() <= 8

def test_shortest_path_within_a_community():
    hotel_poi_id = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"

    g_tmp, p = project_gds_model()
    k = generate_kmeans_model(g_tmp)
    days = k.groupby('communityId')
    days_df = {community_id: df for community_id, df in days}
    result = get_shortest_path(days_df, hotel_poi_id, 0)

    print(result)

    assert result[0]['sourceNodeName'] == 'Park Hyatt Paris-Vendôme'

def test_compute_itinary_for_a_day():
    hotel_poi_id = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"

    g_tmp, p = project_gds_model()
    k = generate_kmeans_model(g_tmp)
    days = k.groupby('communityId')
    days_df = {community_id: df for community_id, df in days}

    hotel_node = get_nodes_by_poi_ids([hotel_poi_id])[0]
    itinary_df = days_df[0]

    # from a starting point I want to compute the shortest path to all other nodes
    step = [hotel_node]
    for node in itinary_df['poi_id']:

        result = get_shortest_path(days_df, hotel_node, node)
        print(result)
    result = get_shortest_path(days_df, start, 0)

    print(result)

    assert false