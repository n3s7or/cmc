import services


async def quotes(payload: dict) -> dict:
    """Requests the cryptocurrencies/quotes endpoint

    https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest

    Args:
        payload: filters/parameters
    """

    return (await services.call('/v1/cryptocurrency/quotes/latest', payload=payload)).json()


async def map_() -> dict:
    """Requests the /v1/cryptocurrency/map endpoint

    https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap

    Args:
    """

    return (await services.call('/v1/cryptocurrency/map')).json()
