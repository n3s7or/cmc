import os
from pprint import pprint
import requests


BASE_URL = 'https://pro-api.coinmarketcap.com'
API_KEY = os.environ.get('HX_CMC_APIKEY')


def _call(endpoint: str, payload: dict) -> dict:
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'deflate, gzip',
        'X-CMC_PRO_API_KEY': API_KEY
        }

    url = BASE_URL + endpoint

    return requests.get(url, headers=headers, params=payload).json()    # TODO: implement retry logic and error handling


def quotes(id_arr: list) -> dict:
    """Returns the latest market quote for 1 or more cryptocurrencies
    
    Arguments:
    id_arr -- array ids to fetch quotes info

    https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest
    """

    payload = {'id': ','.join(map(lambda i: str(i), id_arr))}
    data = _call('/v1/cryptocurrency/quotes/latest', payload=payload)

    res = {}

    for key, record in data['data'].items():
        res[key] = { field:value 
                        for field, value in record['quote']['USD'].items()
                        if field in [
                                    'price', 'percent_change_24h', 'percent_change_7d', 
                                    'percent_change_30d', 'percent_change_60d', 
                                    'percent_change_90d', 'market_cap'
                                    ]
                    }   # lmao

    return res


def main():    
    id_arr = [1]  # random ids (BTC, LTC, NMC) NMC? namecoin
    pprint(quotes(id_arr))
   

if __name__ == "__main__":
    main()
