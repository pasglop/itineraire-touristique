import json
import os

import pandas as pd
import requests


class itinaryApi:

    def __init__(self):
        self.request = requests
        self.uri = "http://localhost:8000"

    def get_api_status(self):
        return requests.get(self.uri + "/").json()

    def _get_hotel_list(self):
        return requests.get(self.uri + "/poi_by_class/Hotel")

    def get_poi_detail(self, poi_id: str) -> (int, dict):
        response = requests.get(self.uri + f"/poi/{poi_id}")

        if response.status_code == 200 or response.status_code == 402:
            return response.status_code, response.json()

        raise Exception("Error while getting POI details")

    def get_hotel_dataframe(self):
        response = self._get_hotel_list()
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['poi'])
            return df

        return None

    def _create_itinary(self, days: int, poi: str):
        data = {
            "hotel_poi": poi,
            "days": days
        }
        return requests.post(self.uri + "/itinary/",
                             json=data,
                             headers={
                                 'Content-Type': 'application/json'
                             })

    def create_itinary_response(self, days, hotel_poi) -> dict | requests.Response:
        if os.getenv('ENV') == 'test':
            with open(os.path.abspath("stub.json")) as json_file:
                data = json.load(json_file)
                return data['itinary']

        response = self._create_itinary(days, hotel_poi)
        if response.status_code == 200:
            data = response.json()
            return data['itinary']
        return response
