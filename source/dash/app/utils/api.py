import pandas as pd
import requests


class itinaryApi:

    def __init__(self):
        self.request = requests
        self.uri = "http://localhost:8000"

    def getApiStatus(self):
        return requests.get(self.uri + "/").json()

    def _getHotelList(self):
        return requests.get(self.uri + "/poi_by_class/Hotel")

    def getHotelDataframe(self):
        response = self._getHotelList()
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['poi'])
            return df

        return None

    def _createItinary(self, days: int, poi: str):
        data = {
            "hotel_poi": poi,
            "days": days
        }
        print(data)
        return requests.post(self.uri + "/itinary/",
                             json=data,
                             headers={
                                 'Content-Type': 'application/json'
                             })

    def createItinaryDataFrame(self, days, hotel_poi):
        response = self._createItinary(days, hotel_poi)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['itinary'])
            return df

        return None
