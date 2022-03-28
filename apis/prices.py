import requests
from data.config import API_KEY
import json

API_URL = 'https://min-api.cryptocompare.com/data'


class CryptoCompare(object):

    def __init__(self):
        self.base_url = API_URL
        self.api_key = API_KEY

    def __request(self, method, params):
        url = self.base_url + method

        r = requests.get(url = url, params = params)
        res = r.json()
        
        return res

    def get_price(self, ticker, convert='usdt'):
        params = {
            'api_key':self.api_key,
            'fsym': ticker,
            'tsyms': convert
        }
        return self.__request(method = '/price', params=params)