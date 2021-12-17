import asyncio
import services.cmc


async def main():
    id_arr = [1, 2, 2781]  # ids (BTC, LTC, USD)

    print(await services.cmc.get_prices(id_arr))
    print(await services.cmc.get_crypto_data(id_arr))


asyncio.run(main())

