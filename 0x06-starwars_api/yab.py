from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

na = figlet.getFonts()
na = input("input: ")
if len(sys.argv) == 0:
    figlet.setFont(font=random.choice(na))
    print(na)
elif len(sys.argv) == 3:
    figlet.setFont(font= sys.argv[2])
else:
    sys.exit("invalid")

print(figlet.renderText(na))