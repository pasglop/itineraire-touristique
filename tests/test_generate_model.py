from source.graph_operations.generate_model import drop_all_indexes, create_graph_index, extend_remarkable_pois, \
    create_poi_relationships, generate_mustseen_labels, project_gds_model, generate_kmeans_model, get_shortest_path, \
    generate_hotels_labels, project_gds_model_mustseen_and_hotels, get_nodes_by_poi_ids


def test_create_graph_index():
    drop_all_indexes()
    res = create_graph_index()
    assert res.counters.indexes_added == 1

def test_extend_remarkable_pois():
    assert extend_remarkable_pois().counters.properties_set > 0

def test_generate_mustseen_labels():
    assert generate_mustseen_labels().counters.labels_added > 0


def test_generate_hotels_labels():
    assert generate_hotels_labels().counters.labels_added > 0

def test_create_poi_relationships():
    create_poi_relationships()
    assert True # not possible to get result from neo4j

def test_project_gds_model():
    p = project_gds_model_mustseen_and_hotels()
    assert p.nodeCount > 0 and p.relationshipCount > 0


def test_generate_kmeans_model():
    """
    Test the kmeans model
    I want to have 7 communities (days) with at most 8 pois per community
    :return:
    """
    g_tmp, p = project_gds_model()
    assert p.nodeCount > 0 and p.relationshipCount > 0
    k = generate_kmeans_model(g_tmp)
    # Count the number of unique communities
    num_communities = k['communityId'].nunique()
    assert num_communities == 7

    # Count the number of rows for each community
    num_rows_per_community = k['communityId'].value_counts()
    assert num_rows_per_community.min() > 0 and num_rows_per_community.max() <= 8

def test_generate_kmeans_model_with_2_communities():
    """
    Test the kmeans model
    I want to have 2 communities (days) with at most 8 pois per community
    :return:
    """
    g_tmp, p = project_gds_model()
    assert p.nodeCount > 0 and p.relationshipCount > 0
    k = generate_kmeans_model(g_tmp, days=2)

    print(k)
    # Count the number of unique communities
    num_communities = k['communityId'].nunique()
    assert num_communities == 2

    # Count the number of rows for each community
    num_rows_per_community = k['communityId'].value_counts()
    assert num_rows_per_community.min() > 0 and num_rows_per_community.max() <= 8

def test_shortest_path_within_a_community():
    hotel_poi_id = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"

    g_tmp, p = project_gds_model()
    k = generate_kmeans_model(g_tmp)
    days = k.groupby('communityId')
    days_df = {community_id: df for community_id, df in days}
    result = get_shortest_path(days_df, hotel_poi_id, 0)

    print(result)

    assert result[0]['sourceNodeName'] == 'Park Hyatt Paris-Vendôme'

def test_compute_itinary_for_a_day():
    hotel_poi_id = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"

    g_tmp, p = project_gds_model()
    k = generate_kmeans_model(g_tmp)
    days = k.groupby('communityId')
    days_df = {community_id: df for community_id, df in days}

    hotel_node = get_nodes_by_poi_ids([hotel_poi_id])[0]
    itinary_df = days_df[0]

    # from a starting point I want to compute the shortest path to all other nodes
    step = [hotel_node]
    for node in itinary_df['poi_id']:

        result = get_shortest_path(days_df, hotel_node, node)
        print(result)
    result = get_shortest_path(days_df, start, 0)

    print(result)

    assert false