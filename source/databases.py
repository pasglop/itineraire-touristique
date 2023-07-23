import os

import psycopg2
import psycopg2.extras
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
    sess = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
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


def query_graph(query):
    db = connect_neo4j()
    records, summary, keys = db.execute_query(query)
    disconnect_neo4j(db)
    # Summary information
    print("The query `{query}` returned {records_count} records in {time} ms.".format(
        query=summary.query, records_count=len(records),
        time=summary.result_available_after
    ))
    # Loop through results
    result = []
    for record in records:
        result.append(record.data())

    return result


def create_graph(query):
    db = connect_neo4j()
    result = db.execute_query(query).summary
    disconnect_neo4j(db)
    return result


def reset_graph(node_type=None):
    if node_type:
        result = create_graph(f"MATCH (n:{node_type}) DETACH DELETE n")
    else:
        result = create_graph("MATCH (n) DETACH DELETE n")
    return result
