from . import _call


def quotes(id_arr: list) -> list:
    """Returns the latest market quote for 1 or more cryptocurrencies
    
    Arguments:
    id_arr -- array ids to fetch quotes info

    https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest
    """

    payload = {'id': ','.join(map(lambda i: str(i), id_arr))}
    data = _call('/v1/cryptocurrency/quotes/latest', payload=payload)

    res = []

    for key, record in data['data'].items():
        crypto = { field:value 
                        for field, value in record['quote']['USD'].items()
                        if field in [
                                    'price', 'percent_change_24h', 'percent_change_7d', 
                                    'percent_change_30d', 'percent_change_60d', 
                                    'percent_change_90d', 'market_cap'
                                    ]
                    }   # lmao
        crypto['id'] = key
        res.append(crypto)

    return res
