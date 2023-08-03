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
