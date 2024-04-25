from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

na = figlet.getFonts()
na = input("input: ")
if len(sys.argv) == 1:
    israndomFont = True
elif len(sys.argv) == 3:
    Figlet.setFont(font= sys.argv[2])
else:
    sys.exit("invalid")
print(figlet.renderText(na))