import requests
import sys

n = 38,761.0833

while True:
    try:
        if len(sys.argv) == 1:
            n = n * 2
        response = requests.get("https://api.coindesk.com/v1/bpi/cuuremtprice.json"+ sys.argv[1])
        print(response.json())
    except requests.RequestException:
        sys.exit("not a command-line argument")

