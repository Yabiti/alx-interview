import requests
import sys

amount = 345465

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" + sys.argv[1])
print(response.json())