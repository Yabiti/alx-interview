import sys
import requests

amount = 3445.55

try:
    for arg in sys.argv[1:]:
        amount = amount * float(input("$"))
        print(f"${amount: .4f}")
except requests.RequestException:
    sys.exit("not a command-line argument")