from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

available_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    chosen_font = random.choice(available_fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in available_fonts:
        sys.exit("Invalid usage")


    chosen_font = sys.argv[2]

else:
    sys.exit("Invalid usage")


figlet.setFont(font=chosen_font)

user_text = input("Input: ")
print(figlet.renderText(user_text))
