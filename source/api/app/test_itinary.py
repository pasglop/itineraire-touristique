from pprint import pprint

import pytest
from fastapi.testclient import TestClient

import dotenv
from pydantic import ValidationError

dotenv.load_dotenv()
from .main import app
from .v1.itinary.itinary_gen import ItinaryGenerator

from .v1.itinary.itinary_models import ItinaryStepVisitSchema, ItinaryStepWalkSchema, VisitDetailSchema, \
    WalkDetailSchema
from .v1.poi import poi_detail_example

step_example = {'costs': [0.0,
                       121.59333071694321,
                       121.59333071694321,
                       160.7601636151291,
                       160.7601636151291,
                       160.7601636151291,
                       226.36740100073297,
                       284.6003777282993,
                       284.6003777282993,
                       323.273152919846],
             'nodeLabels': [['POI', 'MustSeen'],
                            ['Station'],
                            ['StationLine'],
                            ['StationLine'],
                            ['Station'],
                            ['StationLine'],
                            ['StationLine'],
                            ['StationLine'],
                            ['Station'],
                            ['POI', 'MustSeen']],
             'nodeNames': ['Atelier Brancusi - Centre Georges Pompidou',
                           'RAMBUTEAU',
                           'RAMBUTEAU - 11',
                           'HOTELDEVILLE - 11',
                           'HOTELDEVILLE',
                           'HOTELDEVILLE - 1',
                           'STPAUL - 1',
                           'BASTILLE - 1',
                           'BASTILLE',
                           'Opéra national de Paris - Opéra Bastille'],
             'path': [{'coordinates': 'POINT(2.3516667000000098 48.8608333 0.0)',
                       'id': '80f1030e-c06e-bd00-c932-501ba3c3787b',
                       'latitude': 48.8608333,
                       'listOfClass': ['Museum', 'CulturalSite'],
                       'locality': 'Paris',
                       'longitude': 2.3516667000000098,
                       'model_coordinates': [48.8608333, 2.3516667000000098],
                       'mustseen': True,
                       'name': 'Atelier Brancusi - Centre Georges Pompidou',
                       'remarkable': False},
                      {'city': 'Paris',
                       'coordinates': 'POINT(2.35343 48.86119 0.0)',
                       'latitude': 48.86119,
                       'longitude': 2.35343,
                       'name': 'RAMBUTEAU',
                       'station': 'Rambuteau',
                       'stats': 2127291},
                      {'city': 'Paris',
                       'coordinates': 'POINT(2.35343 48.86119 0.0)',
                       'latitude': 48.86119,
                       'longitude': 2.35343,
                       'name': 'RAMBUTEAU - 11',
                       'station': 'Rambuteau',
                       'station_name': 'RAMBUTEAU',
                       'stats': 2127291},
                      {'city': 'Paris',
                       'coordinates': 'POINT(2.351525 48.857487 0.0)',
                       'latitude': 48.857487,
                       'longitude': 2.351525,
                       'name': 'HOTELDEVILLE - 11',
                       'station': 'Hôtel de Ville',
                       'station_name': 'HOTELDEVILLE',
                       'stats': 7251729},
                      {'city': 'Paris',
                       'coordinates': 'POINT(2.351525 48.857487 0.0)',
                       'latitude': 48.857487,
                       'longitude': 2.351525,
                       'name': 'HOTELDEVILLE',
                       'station': 'Hôtel de Ville',
                       'stats': 7251729},
                      {'city': 'Paris',
                       'coordinates': 'POINT(2.351525 48.857487 0.0)',
                       'latitude': 48.857487,
                       'longitude': 2.351525,
                       'name': 'HOTELDEVILLE - 1',
                       'station': 'Hôtel de Ville',
                       'station_name': 'HOTELDEVILLE',
                       'stats': 7251729},
                      {'city': 'Paris',
                       'coordinates': 'POINT(2.360859 48.855214 0.0)',
                       'latitude': 48.855214,
                       'longitude': 2.360859,
                       'name': 'STPAUL - 1',
                       'station': 'Saint-Paul',
                       'station_name': 'STPAUL',
                       'stats': 4295823},
                      {'city': 'Paris',
                       'coordinates': 'POINT(2.369077 48.853082 0.0)',
                       'latitude': 48.853082,
                       'longitude': 2.369077,
                       'name': 'BASTILLE - 1',
                       'station': 'Bastille',
                       'station_name': 'BASTILLE',
                       'stats': 8069243},
                      {'city': 'Paris',
                       'coordinates': 'POINT(2.369077 48.853082 0.0)',
                       'latitude': 48.853082,
                       'longitude': 2.369077,
                       'name': 'BASTILLE',
                       'station': 'Bastille',
                       'stats': 8069243},
                      {'coordinates': 'POINT(2.3694831999999906 48.8533605 0.0)',
                       'id': 'cc4b0d1a-fd1d-4b15-0ceb-501ba3642eb0',
                       'latitude': 48.8533605,
                       'listOfClass': ['RemarkableBuilding', 'CulturalSite'],
                       'locality': 'Paris',
                       'longitude': 2.3694831999999906,
                       'model_coordinates': [48.8533605, 2.3694831999999906],
                       'mustseen': True,
                       'name': 'Opéra national de Paris - Opéra Bastille',
                       'remarkable': False}],
             'sourceNodeName': 'Atelier Brancusi - Centre Georges Pompidou',
             'sourceNodePoiId': '80f1030e-c06e-bd00-c932-501ba3c3787b',
             'targetNodeName': 'Opéra national de Paris - Opéra Bastille',
             'targetNodePoiId': 'cc4b0d1a-fd1d-4b15-0ceb-501ba3642eb0',
             'totalCost': 323.273152919846}

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


def test_should_post_itinary_parameters_and_get_an_itinary():
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

    first_step = igen._find_next_step(igen.days_df[day]['poi_id'].tolist(), hotel_poi_id)
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
    first_step = igen._find_next_step(igen.days_df[day]['poi_id'].tolist(), hotel_poi_id)
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

    for day in range(days):
        assert len(igen.list_steps[day]['steps']) == num_rows_per_community[day]+1


def test_map_steps_to_walking_step():
    igen = ItinaryGenerator()
    path = igen._combine_paths(step_example['path'], step_example['costs'], step_example['nodeLabels'])

    try:
        result = igen._map_to_walk(path[0], path[1])
    except ValidationError as e:
        print(e.json())
        pytest.fail("Should not raise an error")

    assert True

def test_map_steps_to_subway_step():
    igen = ItinaryGenerator()
    path = igen._combine_paths(step_example['path'], step_example['costs'], step_example['nodeLabels'])
    path = path[1:]
    previous_step = path.pop(0)

    try:
        result = igen._map_to_subway(path, previous_step)
    except ValidationError as e:
        print(e.json())
        pytest.fail("Should not raise an error")

    assert True

def test_map_steps_to_visit_step():
    igen = ItinaryGenerator()
    path = igen._combine_paths(step_example['path'], step_example['costs'], step_example['nodeLabels'])

    try:
        result = igen._map_to_visit(path[9])
    except ValidationError as e:
        print(e.json())
        pytest.fail("Should not raise an error")

    assert True

def test_should_map_steps_return_itinary_without_error():
    hotel_poi_id = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"
    days = 2

    igen = ItinaryGenerator()
    try:
        result = igen.generate_itinary(days, hotel_poi_id)
    except ValidationError as e:
        print(e.json())
        pytest.fail("Should not raise an error")

    assert True

def test_should_find_terminal_station():
    igen = ItinaryGenerator()
    path = igen._combine_paths(step_example['path'], step_example['costs'], step_example['nodeLabels'])
    result = igen._find_terminal_station([path[2], path[3]])
    print(path[2])
    print(path[3])
    assert result == 'Châtelet'



# walking_step_detail = WalkDetailSchema({})
# walking_step_params = {
#     'step_detail':  walking_step_detail
# }
#
# with pytest.raises(ValidationError):
#     walking_step = ItinaryStepWalkSchema(walking_step_params)
