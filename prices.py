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


def something(id_arr: list) -> dict:
    payload = {'id': ','.join(map(lambda i: str(i), [1,2,3]))}
    res = _call('/v1/cryptocurrency/quotes/latest', payload=payload)
    return res


def main():
    # pprint(_call('/v1/cryptocurrency/map'))
    # pprint(_call('/v1/cryptocurrency/info?id=1'))    # Let's see xd     - nothing useful here
    id_arr = [1, 2, 3]  # random ids
    pprint(something(id_arr))
    


if __name__ == "__main__":
    main()
