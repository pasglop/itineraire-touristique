import pytest
from geopy.geocoders import Nominatim

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

    def test_should_have_poi_data_with_geo_coordinates(self):
        process = LoadObjects()
        data = process.load_data_from_db(limit=10)
        # essai de validation de l'adresse par geopy (inconsistant pas)
        # geoLoc = Nominatim(user_agent="GetLoc")
        # locname = geoLoc.reverse((data[0][2], data[0][3]), exactly_one=True, language='fr')
        # print(locname)
        # print(data[0][1], data[0][4], data[0][5], data[0][6])
        assert isinstance(data[0][0], int)
        assert isinstance(data[0][1], str)

    def test_generate_csv_file_with_poi(self):
        process = LoadObjects()
        generated = process.generate_csv_file_with_poi()
        assert generated is True

    def test_should_copy_csv_file_to_neo4j(self):
        process = LoadObjects()
        copied = process.copy_csv_file_to_neo4j()
        assert copied is True

    def test_should_create_node_in_neo4j(self):
        process = LoadObjects()
        created = process.create_node_in_neo4j()
        assert created.counters.nodes_created > 0

    def test_should_load_stations(self):
        process = LoadObjects()
        loaded = process.load_stations()
        assert loaded.counters.nodes_created > 0

    def test_should_create_stations(self):
        process = LoadObjects()
        created = process.create_stations()
        assert created.counters.nodes_created > 0
        assert created.counters.relationships_created > 0

    def test_should_create_correspondance(self):
        process = LoadObjects()
        created = process.create_direct_correspondance()
        assert created.counters.relationships_created > 0

    def test_should_create_walk_correspondance(self):
        process = LoadObjects()
        created = process.create_walk_correspondance()
        assert created.counters.relationships_created > 0

    def test_should_create_lines(self):
        process = LoadObjects()
        created = process.create_lines()
        assert created.counters.relationships_created > 0
