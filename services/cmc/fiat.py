import services


async def map_() -> dict:
    """Requests the /v1/fiat/map endpoint

    https://coinmarketcap.com/api/documentation/v1/#operation/getV1FiatMap

    Args:
    """

    return (await services.call('/v1/fiat/map')).json()
