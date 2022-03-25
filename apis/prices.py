import requests
import configparser


API_URL = 'https://min-api.cryptocompare.com/data'


config = configparser.ConfigParser()
config.read_file(open('apis.cfg'))

class CryptoCompare(object):

    def __init__(self):
        self.base_url = API_URL
        self.api_key = config.get('CRYPTOCOMPARE', 'API_KEY')

    def __request(self, method, params):
        url = self.base_url + method

        r = requests.get(url = url, params = params)
        res = r.json()
        
        if res['Response'] == 'Error':
            return 'API Error'
        else:
            return res

    def get_price(self, ticker, convert):
        params = {
            'api_key':self.api_key,
            'fsym': ticker,
            'tsyms': convert
        }
        return self.__request(method = '/price')