import json

import pandas as pd
import pytest
from dash.testing.application_runners import import_app

from .utils.api import itinaryApi


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def test_should_api_connect():
    """
    Request API to check if it is connected
    :return:
    """
    iti = itinaryApi()
    assert iti.get_api_status() == {'Hello': 'World'}


def test_should_get_hotel_list_via_api():
    """
    Request API to get the list of Hotels
    :return:
    """
    iti = itinaryApi()
    response = iti._get_hotel_list()
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
    df = iti.get_hotel_dataframe()

    assert isinstance(df, pd.DataFrame)


def test_should_post_form_parameters_to_itinary_api():
    """
    Post form parameters to itinary API
    :return:
    """
    days = 4
    hotel_poi = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"
    iti = itinaryApi()
    response = iti._create_itinary(days, hotel_poi)
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data['itinary'], dict)
    assert isinstance(data['itinary']['days'], list)
    assert len(data['itinary']['days']) == days


def test_should_get_valid_for_itinary():
    """
    Request API to get the list of Hotels as a dataframe
    :return:
    """
    days = 4
    hotel_poi = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"

    iti = itinaryApi()
    data = iti.create_itinary_response(days, hotel_poi)
    assert len(data['days']) == days
