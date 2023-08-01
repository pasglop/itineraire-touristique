import pytest
from fastapi.testclient import TestClient

import dotenv

dotenv.load_dotenv()
from .main import app
from .v1.itinary.itinary_gen import ItinaryGenerator

from .v1.itinary.itinary_models import ItinaryStepVisitSchema, ItinaryStepWalkSchema, VisitDetailSchema, \
    WalkDetailSchema
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
        "hotel_poi": "226b4112-02fd-bbc4-0a6b-501b9f9d1089",
        "days": 2,
    }
    response = client.post("/itinary", json=payload)
    assert response.status_code == 200
    assert response.json()['itinary_id'] is not None


def test_should_generate_knn_model_default_days():
    """
    Test the kmeans model
    I want to have 7 communities (days) with at most 8 pois per community
    :return:
    """
    igen = ItinaryGenerator()
    igen._create_knn_model()
    # Count the number of unique communities
    num_communities = igen.knn_model['communityId'].nunique()
    # Count the number of rows for each community
    num_rows_per_community = igen.knn_model['communityId'].value_counts()
    assert igen.knn_model is not None
    assert num_communities == 7
    assert num_rows_per_community.min() > 0 and num_rows_per_community.max() <= 8


def test_should_generate_knn_model_with_2_communities():
    """
    Test the kmeans model
    I want to have 2 communities (days) with at most 8 pois per community
    :return:
    """
    igen = ItinaryGenerator()
    igen._create_knn_model(2)
    # Count the number of unique communities
    num_communities = igen.knn_model['communityId'].nunique()
    # Count the number of rows for each community
    num_rows_per_community = igen.knn_model['communityId'].value_counts()
    assert igen.knn_model is not None
    assert num_communities == 2
    assert num_rows_per_community.min() > 0 and num_rows_per_community.max() <= 8


def test_should_find_first_step_within_a_day():
    hotel_poi_id = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"
    day = 0

    igen = ItinaryGenerator()
    igen._create_knn_model()

    igen._init_steps()
    first_step = igen._find_next_step(day, hotel_poi_id)
    igen._add_to_steps(day, first_step)

    assert first_step['sourceNodeName'] == 'Park Hyatt Paris-Vendôme'
    assert igen.list_steps[day]['steps'][0]['sourceNodeName'] == 'Park Hyatt Paris-Vendôme'


def test_should_list_steps_length_equals_days():
    igen = ItinaryGenerator()

    igen._create_knn_model(3)
    num_days = igen.knn_model['communityId'].nunique()
    igen._init_steps()
    assert len(igen.list_steps) == num_days


def test_should_have_a_new_step_in_list_steps():
    hotel_poi_id = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"
    day = 0

    igen = ItinaryGenerator()
    igen._create_knn_model()
    igen._init_steps()
    first_step = igen._find_next_step(day, hotel_poi_id)
    igen._add_to_steps(day, first_step)

    assert len(igen.list_steps[day]['steps']) == 1


def test_compute_itinary_for_a_day():
    hotel_poi_id = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"
    days = 6

    igen = ItinaryGenerator()
    igen._create_knn_model(days)
    igen._init_steps()
    # Count the number of rows for each community

    # run the itinary generation
    igen._compute_itinary(days, hotel_poi_id)

    num_rows_per_community = igen.knn_model['communityId'].value_counts()
    assert len(igen.list_steps[day].steps) == num_rows_per_community[0]
