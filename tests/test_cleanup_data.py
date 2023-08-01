from .context import databases, clean_data


def test_search_similarities():
    clean = clean_data.CleanData()
    assert clean.search_similarities() == True
