import requests
import sys

response = requests.get("")
print(response.json())

amount = 34
try:
    amount = amount * amount
except requests.RequestException:
    sys.exit("not a command-linr argument")