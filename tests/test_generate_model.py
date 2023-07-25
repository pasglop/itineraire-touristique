from source.graph_operations.generate_model import drop_all_indexes, create_graph_index, extend_remarkable_pois


def test_create_graph_index():
    drop_all_indexes()
    res = create_graph_index()
    assert res.counters.indexes_added == 1

def test_extend_remarkable_pois():
    assert extend_remarkable_pois().counters.properties_set > 0
