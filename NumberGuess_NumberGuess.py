"""
Number Guess. Guess on the sum of a pair of dice.
If your guess equals the total value of the dice, you win!
If not, the computer wins.
"""


from random import randint
from time import sleep
import sys


def get_user_guess():
    guess = int(input("Guess a number: "))
    return guess


def try_again():
    choice = str(input("Play again (Y/N)?\n>"))
    choice = choice.upper()
    if choice == 'Y':
        print("Restarting...")
        sleep(3)
        roll_dice(6)
    else:
        sys.exit("Exiting...")
    return choice


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print("The maximum possible value is {}".format(max_val))
    guess = get_user_guess()
    while True:
        if guess > max_val:
            print("Invalid guess, maximum possible value is {}".format(max_val))
            break
        else:
            print("Rolling...")
            sleep(2)
            print("The first roll is {}".format(first_roll))
            sleep(1)
            print("The second roll is {}".format(second_roll))
            sleep(1)
            total_roll = first_roll + second_roll
            print(total_roll)
            print("Result...")
            sleep(1)
            if guess == total_roll:
                print("Congratulations, you won!")
            else:
                print("Better luck next time!")
        break


roll_dice(6)
try_again()
