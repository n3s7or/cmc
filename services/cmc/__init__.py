import httpx
from httpx import codes
from services.cmc import cryptocurrency, fiat
from settings import logger


def check_cmc_status(response: httpx.Response):
    response_data = response.json()

    if response.status_code == codes.too_many_requests:
        logger.info("[%s]-%s on request to %s".format(
                                                    response.status_code,
                                                    response_data['status']['error_message'],
                                                    response.url
                                                    ))
        return True

    if response.status_code in [codes.BAD_REQUEST, codes.UNAUTHORIZED, codes.PAYMENT_REQUIRED,
                                codes.FORBIDDEN, codes.INTERNAL_SERVER_ERROR]:
        logger.warning("[{}] - {} on request to {}".format(
                                                    response.status_code,
                                                    response_data['status']['error_message'],
                                                    response.url
                                                    ))

    return False


def _select_records_from_quote(data: dict, fields: list) -> list:
    """Extract desired fields from quote data from default currency (USD)"""

    res = []
    for key, record in data['data'].items():
        crypto = {field: value
                  for field, value in record['quote']['USD'].items()
                  if field in fields}
        crypto['id'] = key
        res.append(crypto)
    return res


async def get_crypto_data(id_arr: list) -> list:
    """Returns the latest prices, percent change and cap for 1 or more (crypto)currencies

    Args:
        id_arr: list of coinmarketcap ids to fetch quotes info
    """

    payload = {'id': ','.join(map(lambda i: str(i), id_arr))}
    json_response = await cryptocurrency.quotes(payload)
    res = []

    if 'data' not in json_response:
        logger.info('Returning empty list, probably error while fetching data')
        return res

    return _select_records_from_quote(
        json_response,
        [
          'price', 'percent_change_24h', 'percent_change_7d',
          'percent_change_30d', 'percent_change_60d',
          'percent_change_90d', 'market_cap',
        ])


async def get_prices(id_arr: list):
    """Returns the latest prices USD based for 1 or more (crypto)currencies

    Args:
        id_arr: list of coinmarketcap ids to fetch quotes info
    """

    payload = {'id': ','.join(map(lambda i: str(i), id_arr))}
    json_response = await cryptocurrency.quotes(payload)

    res = []

    if 'data' not in json_response:
        logger.info('Returning empty list, probably error while fetching data')
        return res

    return _select_records_from_quote(json_response, ['price'])


async def get_fiat_map() -> list:
    """Returns a mapping of all supported fiat currencies to unique CoinMarketCap ids"""

    # Todo: maybe implement pagination

    json_response = await fiat.map_()

    if 'data' not in json_response:
        logger.info('Returning empty list, probably error while fetching data')
        return []

    return json_response.get('data')


async def get_cryptocurrency_map() -> list:
    """Returns a mapping of all cryptocurrencies to unique CoinMarketCap ids"""

    # Todo: maybe implement pagination

    json_response = await cryptocurrency.map_()

    if 'data' not in json_response:
        logger.info('Returning empty list, probably error while fetching data')
        return []

    return json_response.get('data')
