import services


async def quotes(payload: dict) -> dict:
    """Requests the cryptocurrencies/quotes endpoint

    https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest

    Args:
        payload: filters/parameters
    """

    return (await services.call('/v1/cryptocurrency/quotes/latest', payload=payload)).json()
