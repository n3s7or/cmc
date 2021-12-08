import backoff
import requests
from requests import codes
from requests.exceptions import RequestException, ConnectionError, Timeout
from settings import logger, BASE_URL, API_KEY


def check_cmc_status(response: requests.Response):
    response_data = response.json()

    if response.status_code == requests.codes.too_many_requests:
        logger.info("[%s]-%s on request to %s".format(
                                                    response.status_code,
                                                    response_data['status']['error_message'],
                                                    response.url
                                                    ))
        return True

    if response.status_code in [codes.bad, codes.unauthorized, codes.payment_required, codes.forbidden, codes.server_error]:
        logger.warning("[{}]-{} on request to {}".format(
                                                    response.status_code,
                                                    response_data['status']['error_message'],
                                                    response.url
                                                    ))

    return False


@backoff.on_predicate(                                                  # Check if we hit any 4XX or 500 error
                    backoff.constant, 
                    check_cmc_status,
                    max_tries=3,
                    jitter=backoff.random_jitter,
                    interval=4,
                    logger=logger
                    )
@backoff.on_exception(backoff.expo,
                    (RequestException, ConnectionError, Timeout),       # retry for any of those errors
                    max_time=30,                                        # max wait 30 seconds
                    max_tries=3,                                        # self explanatory
                    logger=logger
                    )
def _call(endpoint: str, payload: dict) -> requests.Response:
    """Creates HTTP requests
    
    This function will retry three times if any of the following
    exceptions occur (RequestException, ConnectionError, Timeout)
    
    Arguments:
    endpoint : str  -- coinmarketcap endpoint to request
    payload  : dict -- url parameters
    """
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'deflate, gzip',
        'X-CMC_PRO_API_KEY': API_KEY
        }
    

    return requests.get(BASE_URL + endpoint, headers=headers, params=payload)
