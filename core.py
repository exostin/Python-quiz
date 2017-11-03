import sys
import webbrowser
import os

# Defining dash, because in windows it is \ while in linux/mac it is /
if os.name == 'nt':
    dash = "\\"
else:
    dash = "/"
# Changing path to another directory to import functions from it
sys.path.append("functions{}".format(dash))
from quiz import main_quiz
from read import main_read
from fill import main_fill

try:
    while True:
        print('''Quiz (q) - take the quiz
Read (r) - read scores from quiz
Fill (f) - make your own question set for quiz
GitHub (git) - Launches this project link in your default browser
Nevermind (nvm) - Exit''')
        while True:
            choice = input('Enter your choice: ').lower()
            if choice == 'q':
                main_quiz()
                break
            elif choice == 'r':
                main_read()
                break
            elif choice == 'f':
                main_fill()
                break
            elif choice == "git":
                webbrowser.open("https://github.com/exostin/Python-quiz")
                break
            elif choice == 'nvm':
                sys.exit(0)
            else:
                print("Wrong input! Try again.")
                continue
        again = input('Do you want to do something more? [y/n] ').lower()
        if again == 'y':
            continue
        else:
            break
except KeyboardInterrupt:
    print("Shutdown requested...exiting")
