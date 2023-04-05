import sys
import os

from src.game import game
from src.main_menu.help_menu import help_option


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
        start()
    elif option.lower() == 'quit':
        sys.exit()
    else:
        print("Invalid command. Please choose 'play', 'help', or 'quit'.")
        choose_option()
