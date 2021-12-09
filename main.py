import services.cmc


def main():    
    id_arr = [1, 2, 2781]  # ids (BTC, LTC, USD)

    print(services.cmc.get_prices(id_arr))
    # print(services.cmc.get_crypto_data(id_arr))


if __name__ == "__main__":
    main()
