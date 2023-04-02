import sys
import os

from game import game


def start():
    os.system('clear')
    print('################################')
    print('# Welcome to the Mystery Game! #')
    print('################################')
    print('           .: Play :.           ')
    print('           .: Help :.           ')
    print('           .: Quit :.           ')
    sys.stdout.flush()
    choose_option()


def choose_option():
    option = input("> ")
    if option.lower() == 'play':
        game.start_game()
    elif option.lower() == 'help':
        help_option()
    elif option.lower() == 'quit':
        sys.exit()
    else:
        print("Invalid command. Please choose 'play', 'help', or 'quit'.")
        choose_option()


def help_option():
    print('################################')
    print('# Welcome to the Mystery Game! #')
    print('################################')
    print('- Use up, down, left, right to move.')
    print('- Type your commands to do them.')
    print('- Use "examine" to inspect something.')
    print('- Use "take" to put item in a bag.')
    print('- Good luck and have fun!\n')
    print("Press the 'Enter' key to return to the main menu.")

    input()
    start()
