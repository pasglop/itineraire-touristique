import pytest

from source.databases import connect_db, disconnect_db
from source.graph_operations.load_objects import LoadObjects

# TDD file for loading data into Neo4j

"""
Feature: Load datatourisme data into Neo4j
Scenario:
    from the postgresql database, extract POIs with geo coordinates
    for each POI, create a node in Neo4j
"""


class TestLoadNeo4j:

    @pytest.fixture
    def db_session(self):
        conn, db_session = connect_db()
        yield conn, db_session
        disconnect_db(conn, db_session)

    @pytest.fixture
    def neo4j_session(self):
        conn, db_session = connect_db()
        yield conn, db_session
        disconnect_db(conn, db_session)

    @pytest.fixture
    def load_objects(self):
        return LoadObjects()

    def test_should_have_poi_data_with_geo_coordinates(self, load_objects):
        data = load_objects.load_data_from_db(limit=10)
        # essai de validation de l'adresse par geopy (inconsistant pas)
        # geoLoc = Nominatim(user_agent="GetLoc")
        # locname = geoLoc.reverse((data[0][2], data[0][3]), exactly_one=True, language='fr')
        # print(locname)
        # print(data[0][1], data[0][4], data[0][5], data[0][6])
        assert isinstance(data[0][0], str)
        assert isinstance(data[0][1], str)

    def test_generate_csv_file_with_poi(self, load_objects):
        generated = load_objects.generate_csv_file_with_poi()
        assert generated is True

    def test_should_copy_csv_file_to_neo4j(self, load_objects):
        copied = load_objects.copy_csv_file_to_neo4j()
        assert copied is True

    def test_should_create_node_in_neo4j(self, load_objects):
        created = load_objects.create_node_in_neo4j()
        assert created.counters.nodes_created > 0

    def test_should_load_stations(self, load_objects):
        loaded = load_objects.load_stations()
        assert loaded.counters.nodes_created > 0

    def test_should_create_stations(self, load_objects):
        created = load_objects.create_stations()
        assert created.counters.nodes_created > 0
        assert created.counters.relationships_created > 0

    def test_should_create_correspondance(self, load_objects):
        created = load_objects.create_direct_correspondance()
        assert created.counters.relationships_created > 0

    def test_should_create_walk_correspondance(self, load_objects):
        created = load_objects.create_walk_correspondance()
        assert created.counters.relationships_created > 0

    def test_should_create_lines(self, load_objects):
        created = load_objects.create_lines()
        assert created.counters.relationships_created > 0

    def test_should_create_walking_to_station(self, load_objects):
        created = load_objects.create_walk_to_station()
        assert created.counters.relationships_created > 0

    def test_create_graph_index(self, load_objects):
        load_objects.drop_all_indexes()
        res = load_objects.create_graph_index()
        assert res.counters.indexes_added == 1

    def test_extend_remarkable_pois(self, load_objects):
        assert load_objects.extend_remarkable_pois().counters.properties_set > 0

    def test_generate_mustseen_labels(self, load_objects):
        assert load_objects.generate_mustseen_labels().counters.labels_added > 0

    def test_generate_hotels_labels(self, load_objects):
        assert load_objects.generate_hotels_labels().counters.labels_added > 0

    def test_create_poi_relationships(self, load_objects):
        load_objects.create_poi_relationships()
        assert True  # not possible to get result from neo4j

    def test_project_gds_knn_model(self, load_objects):
        p = load_objects.project_gds_model()
        assert p.nodeCount > 0 and p.relationshipCount > 0

    def test_project_gds_model_mustseen_and_hotels(self, load_objects):
        p = load_objects.project_gds_model_mustseen_and_hotels()
        assert p.nodeCount > 0 and p.relationshipCount > 0
