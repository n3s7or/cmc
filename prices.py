import services.endpoints
from pprint import pprint


def main():    
    id_arr = [1, 2, 8]  # random ids (BTC, LTC, NMC) NMC? namecoin

    res = services.endpoints.quotes(id_arr)
    
    pprint(res)
   

if __name__ == "__main__":
    main()
