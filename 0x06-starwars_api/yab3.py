import sys
import requests

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        sys.exit("command line argument is not a number")
else:
    sys.exit("missing line argument")
try:
    response = requests.get("htpps://api.coinbreak.com/v1/bpi/currentprice.json")
    print(response['bpi']['usd']['rate_float'])
    amount = value * value
except requests.RequestException:
    sys.exit()