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

    def test_should_have_poi_data_with_geo_coordinates(self):
        process = LoadObjects()
        data = process.load_data_from_db()
        assert data[0]['geo_coordinates'] is not None
