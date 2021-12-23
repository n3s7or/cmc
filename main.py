import asyncio
import services.cmc
from pprint import pprint


async def main():
    id_arr = [1, 2, 2781]  # ids (BTC, LTC, USD)

    # pprint(await services.cmc.get_prices(id_arr))
    # pprint(await services.cmc.get_crypto_data(id_arr))
    # pprint(await services.cmc.get_fiat_map())
    pprint(await services.cmc.get_cryptocurrenciy_map())


asyncio.run(main())

