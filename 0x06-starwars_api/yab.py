from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

na = figlet.getFonts()

if len(sys.argv) == 0:
    input("input: ")
    figlet.setFont(font=random.choice(na))
elif len(sys.argv) == 3:
    for s in na:
        print(figlet.renderText(s))
else:
    figlet.setFont(font=random.choice(na))
