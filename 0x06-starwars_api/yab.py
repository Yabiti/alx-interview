from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

na = figlet.getFonts()

if len(sys.argv) == 0:
    random.shuffle(na)
elif len(sys.argv) == 2:
    for s in na:
        print(figlet.renderText(s))
else:
    sys.exit("Error")