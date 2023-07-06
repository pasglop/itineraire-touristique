import os

import psycopg2
from neo4j import GraphDatabase


def connect_db():
    """
    This function is used to connect to the postgresql database.
    :return:
    """
    conn = psycopg2.connect(
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"))
    sess = conn.cursor()
    return conn, sess


def disconnect_db(conn, sess):
    sess.close()
    conn.close()


def connect_neo4j():
    """
    This function is used to connect to the neo4j database.
    """
    host = os.getenv("NEO4J_CONTAINER")
    bolt_port = os.getenv("NEO4J_BOLT_PORT")
    uri = f"bolt://{host}:{bolt_port}"
    return GraphDatabase.driver(uri, auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD")))


def disconnect_neo4j(driver):
    driver.close()
