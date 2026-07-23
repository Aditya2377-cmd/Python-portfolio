import requests
import json


response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")

data = response.json()
print(data["bpi"]["USD"]["rate"])
