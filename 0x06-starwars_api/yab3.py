import requests
import sys

amount = 345465
amount = float(amount * 2)
print(amount)
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" + sys.argv[1])
print(response.json())

try:
    amount = float()
except requests.RequestException:
    sys.exit("not a command line argument")
