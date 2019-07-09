apiKey = "3d962fc56013560002625148bb9d05b2713e2415f63cf9bf25ccab7612b0de6f"

url = "https://min-api.cryptocompare.com/data/price"

payload = {
    "fsym": "BTC",
    "tsyms": "USD"
}

headers = {
    "authorization": "Apikey " + apiKey
}