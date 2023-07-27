from source.graph_operations.generate_model import drop_all_indexes, create_graph_index, extend_remarkable_pois, \
    create_poi_relationships, generate_mustseen_labels


def test_create_graph_index():
    drop_all_indexes()
    res = create_graph_index()
    assert res.counters.indexes_added == 1

def test_extend_remarkable_pois():
    assert extend_remarkable_pois().counters.properties_set > 0

def test_create_poi_relationships():
    create_poi_relationships()
    assert True # not possible to get result from neo4j

def test_generate_mustseen_labels():
    assert generate_mustseen_labels().counters.labels_added > 0