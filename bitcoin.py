import sys
import requests
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:

    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Failed to fetch price")

total = bitcoins * price
print(f"${total:,.4f}")
