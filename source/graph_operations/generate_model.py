from dotenv import load_dotenv

from source.databases import create_graph

load_dotenv()  # take environment variables from .env.


def drop_all_indexes():
    summary = create_graph("CALL apoc.schema.assert({},{},true) YIELD label, key RETURN * ")
    print("Dropping all indexes")
    return summary


def create_graph_index():
    create_graph("CREATE INDEX ON :POI(id)")
    summary = create_graph("CREATE INDEX ON :POI(coordinates)")
    print("Creation of index on POI(id) and POI(coordinates)")
    return summary


def extend_remarkable_pois():
    # create a new label RemarkablePOI
    # create a new index on RemarkablePO
    query = """
    LOAD CSV WITH HEADERS FROM 'file:///mustseen.csv' AS row
    MATCH (poi:POI {id: toInteger(row.id)})
    SET poi:MustSeen, poi.mustseen = true, poi.remarkable = toBoolean(row.remarkable)
    """
    summary = create_graph(query)
    return summary


if __file__ == "__main__":
    drop_all_indexes()
    create_graph_index()
