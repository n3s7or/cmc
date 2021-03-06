import backoff
import httpx
from httpx import TimeoutException, NetworkError
from settings import logger, BASE_URL, API_KEY
from .cmc import check_cmc_status


@backoff.on_predicate(                                                  # Check if we hit any 4XX or 500 error
                    backoff.constant,
                    check_cmc_status,
                    max_tries=3,
                    jitter=backoff.random_jitter,
                    interval=4,
                    logger=logger
                    )
@backoff.on_exception(backoff.expo,
                    (NetworkError, TimeoutException),       # retry for any of those errors
                    max_time=30,                                        # max wait 30 seconds
                    max_tries=3,                                        # self explanatory
                    logger=logger
                    )
async def call(endpoint: str, payload: dict = None) -> httpx.Response:
    """Creates HTTP requests
    
    This function will retry three times if any of the following
    exceptions occur (NetworkError, TimeoutException)
    
    Arguments:
    endpoint : str  -- coinmarketcap endpoint to request
    payload  : dict -- url parameters
    """
    if payload is None:
        payload = {}

    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'deflate, gzip',
        'X-CMC_PRO_API_KEY': API_KEY
        }

    aclient = httpx.AsyncClient()
    try:
        res = await aclient.get(BASE_URL + endpoint, headers=headers, params=payload)
        return res
    finally:
        await aclient.aclose()
