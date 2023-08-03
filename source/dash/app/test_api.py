import pandas as pd
import pytest
from dash.testing.application_runners import import_app

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


def test_should_post_form_parameters_to_itinary_api():
    """
    Post form parameters to itinary API
    :return:
    """
    days = 4
    hotel_poi = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"
    iti = itinaryApi()
    response = iti._createItinary(days, hotel_poi)
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data['itinary'], dict)
    assert isinstance(data['itinary']['days'], list)
    assert len(data['itinary']['days']) == days


def test_should_get_dataframe_for_itinary():
    """
    Request API to get the list of Hotels as a dataframe
    :return:
    """
    days = 4
    hotel_poi = "226b4112-02fd-bbc4-0a6b-501b9f9d1089"

    iti = itinaryApi()
    df = iti.createItinaryDataFrame(days, hotel_poi)
    assert isinstance(df, pd.DataFrame)

def test_should_display_itinary_from_post_request(dash_br):
    """
    Post form parameters to itinary API
    :return:
    """

    app = import_app("app")
    dash_br.start_server(app)

    days_input = dash_br.find_element("#visitdays")
    hotel_input = dash_br.find_element("#basehotel")
    submit_button = dash_br.find_element("#submit-button")

    days_input.send_keys("4")
    hotel_input.send_keys("226b4112-02fd-bbc4-0a6b-501b9f9d1089")
    submit_button.click()

    output = dash_br.find_element("#output")

    assert output.text == "Name: John Doe, Email: john.doe@example.com"

    assert False
