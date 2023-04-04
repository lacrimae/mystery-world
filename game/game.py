from constants import dialog
from game.examine import examine
from game.move import move
from game.take import take
from main_menu.help_menu import help_option
from models.player import player, valid_classes, set_class, print_location
from utils.type_util import print_slow

import os
import sys

available_actions = ['quit', 'move', 'help', 'whereami', 'examine', 'take']


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
        if clazz in valid_classes:
            set_class(clazz)
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
        print_location()
    elif action == 'examine':
        examine()
    elif action == 'take':
        take()
    # elif action.lower() in available_actions['TAKE']:
    #     take()
