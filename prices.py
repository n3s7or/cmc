import os
import requests

BASE_URL = 'https://pro-api.coinmarketcap.com'
API_KEY = os.environ.get('HX_CMC_APIKEY')


def _call(endpoint: str) -> dict:
    headers = {'X-CMC_PRO_API_KEY': API_KEY}
    url = BASE_URL + endpoint
    return requests.get(url, headers=headers).json()


def main():
    print(_call('/v1/cryptocurrency/map'))


if __name__ == "__main__":
    main()
