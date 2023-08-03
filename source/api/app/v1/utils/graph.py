import os
import logging
from neo4j import GraphDatabase
from graphdatascience import GraphDataScience


def connect_gds():
    bolt_url = url_neo4j()
    return GraphDataScience(bolt_url, auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD")))


def url_neo4j():
    """
    This function is used to connect to the neo4j database.
    """
    host = os.getenv("NEO4J_HOST")
    bolt_port = os.getenv("NEO4J_BOLT_PORT")
    uri = f"bolt://{host}:{bolt_port}"
    return uri


def connect_neo4j():
    """
    This function is used to connect to the neo4j database.
    """
    host = os.getenv("NEO4J_CONTAINER")
    bolt_port = os.getenv("NEO4J_BOLT_PORT")
    uri = url_neo4j()
    return GraphDatabase.driver(uri, auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD")))


def disconnect_neo4j(driver):
    driver.close()


def query_graph(query):
    db = connect_neo4j()
    records, summary, keys = db.execute_query(query)
    disconnect_neo4j(db)
    # Summary information
    logging.info("The query `{query}` returned {records_count} records in {time} ms.".format(
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
