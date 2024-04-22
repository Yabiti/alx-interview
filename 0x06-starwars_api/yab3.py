import sys
import requests

try:
    
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print(response.json())
except requests.RequestException:
    sys.exit("not a command-line argument")