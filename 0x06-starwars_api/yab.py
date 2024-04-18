from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

na = figlet.getFonts()

if len(sys.argv) == 0:
    random.shuffle(na)
