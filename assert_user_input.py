#! /usr/bin/env python3

#This file shows using the assert statement within a try-except block
#to validate the user's input.

#In this example, we want the user to select an option from 0-5
#Options 1-5 will continue on with the code
#Option 0 will exit the application

import sys #To close the program cleanly.

def select_choice_try_except():
    user_selection = -1
    while user_selection < 0:
        print("[1] Continue 1")
        print("[2] Continue 2")
        print("[3] Continue 3")
        print("[4] Continue 4")
        print("[5] Continue 5")
        print("[0] Exit")
        user_attempted_selection = input("Please choose an option: ")
        try:
            user_attempted_selection = int(user_attempted_selection)
            assert 0 <= user_attempted_selection <= 5
            user_selection = user_attempted_selection
        except ValueError: #Checking to see if the user inputed nonsense data, such as something that is not an integer.
            print("You did not select a number. Please stop trying to break my program")
            continue
        except AssertionError:
            print("You did not select an option between 0 and 5.")
            continue
        else:
            print("You have selected {}. Thank you for your input.".format(user_selection))
            if user_selection == 0:
                print("Goodbye")
                sys.exit(0)


if __name__ == '__main__':
    select_choice_try_except()
