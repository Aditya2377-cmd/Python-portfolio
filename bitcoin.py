import sys
import requests
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:

    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apikey=Yourapikey")
    data = response.json()
    price = float(data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Failed to fetch price")

total = bitcoins * price
print(f"${total:,.4f}")
