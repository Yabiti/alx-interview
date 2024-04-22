import requests
import sys

amount = 38,761.0833
if len(sys.argv) == 1:
        print(f"${amount: .4f}")
while True:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/cuuremtprice.json"+ sys.argv[1])
        print(response.json())
    except requests.RequestException:
        sys.exit("not a command-line argument")

