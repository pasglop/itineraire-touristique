import pandas as pd

from .utils.api import itinaryApi


def test_should_api_connect():
    """
    Request API to check if it is connected
    :return:
    """
    iti = itinaryApi()
    assert iti.getApiStatus() == {'Hello': 'World'}

def test_should_get_hotel_list_via_api():
    """
    Request API to get the list of Hotels
    :return:
    """
    iti = itinaryApi()
    response = iti._getHotelList()
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data['poi'], list)
    assert len(data['poi']) > 0

def test_should_get_dataframe_for_hotel_list():
    """
    Request API to get the list of Hotels as a dataframe
    :return:
    """
    iti = itinaryApi()
    df = iti.getHotelDataframe()

    assert isinstance(df, pd.DataFrame)
