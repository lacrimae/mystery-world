from src.constants import dialog
from src.game.examine import examine
from src.game.move import move
from src.game.take import take
from src.main_menu.help_menu import help_option
from src.model.player import player, VALID_CLASSES
from src.utils.type_util import print_slow

import os
import sys

available_actions = ['quit', 'move', 'help', 'whereami', 'examine', 'take', 'inventory']


def start_game():
    setup()
    play()


def setup():
    os.system('clear')

    # NAME
    print_slow(dialog.SETUP_1)
    player.name = input('> ')

    # CLASS
    print_slow(dialog.SETUP_2.format(player.name))
    print(dialog.SETUP_2_1)

    while True:
        clazz = input('> ').lower()
        if clazz in VALID_CLASSES:
            player.set_class(clazz)
            break
        else:
            print(dialog.SETUP_2_2)

    print_slow(dialog.SETUP_3.format(clazz.capitalize()))

    print(dialog.CONTINUE)
    input()

    os.system('clear')
    print("####################")
    print("# Let's start now! #")
    print("####################")


def play():
    while player.game_over is False:
        prompt()


def prompt():
    print('\n╔══════════════════════════╗')
    print('|What would you like to do?|')
    print('╚══════════════════════════╝\n')
    print("To view available actions, type 'help'.")
    action = input('> ')

    while not any(action.lower() in actions for actions in available_actions):
        print('Unknown action, try again.\n')
        action = input('> ').lower()

    if action == 'quit':
        sys.exit()
    elif action == 'help':
        help_option()
    elif action == 'move':
        move()
    elif action == 'whereami':
        player.print_location()
    elif action == 'examine':
        examine()
    elif action == 'take':
        take()
    elif action == 'inventory':
        player.open_inventory()
