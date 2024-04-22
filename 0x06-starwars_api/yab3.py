import requests
import sys

n = 38,761.0833

try:
    if len(sys.argv) != float:
        sys.exit()
    response = requests.get("https://api.coindesk.com/v1/bpi/cuuremtprice.json")
    print(response.json())
except requests.RequestException:
    sys.exit()