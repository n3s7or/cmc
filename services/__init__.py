import requests
from settings import logger, BASE_URL, API_KEY


def _call(endpoint: str, payload: dict) -> dict:
    """Creates HTTP requests
    
    Arguments:
    endpoint : str  -- coinmarketcap endpoint to request
    payload  : dict -- url parameters
    """
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'deflate, gzip',
        'X-CMC_PRO_API_KEY': API_KEY
        }

    url = BASE_URL + endpoint

    return requests.get(url, headers=headers, params=payload).json()    # TODO: implement retry logic and error handling
