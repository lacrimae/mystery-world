from constants import dialog
from models.player import player, valid_classes, set_class
from utils.type_util import print_slow
from map import zone_map

import os
import sys

available_actions = ['quit', 'move']


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
        action = input('> ')

    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'move':
        move()
    # elif action.lower() in available_actions['EXAMINE']:
    # examine()
    # elif action.lower() in available_actions['TAKE']:
    #     take()


def move():
    print_slow('Where would you like to move?\n')
    handle_moves()


def handle_moves():
    movements = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}

    direction = input("> ").lower().strip()
    x, y = player.location

    if direction not in movements:
        print("Please select a valid direction. Your options are North, South, West, or East.")
        handle_moves()

    dx, dy = movements[direction]
    new_x, new_y = x + dx, y + dy

    if new_x < 0:
        print_slow(dialog.MOVE_LIMIT_NORTH)
        print(dialog.CONTINUE)
        input()
        return
    elif new_x >= len(zone_map[y]):
        print_slow(dialog.MOVE_LIMIT_SOUTH)
        print(dialog.CONTINUE)
        input()
        return
    elif new_y < 0:
        print_slow(dialog.MOVE_LIMIT_SOUTH)
        print(dialog.CONTINUE)
        input()
        return
    elif new_y >= len(zone_map):
        print_slow(dialog.MOVE_LIMIT_SOUTH)
        print(dialog.CONTINUE)
        input()
        return

    print(f"You have traveled to the {direction.capitalize()}.")
    player.location = [new_x, new_y]


def print_location():
    x, y = player.location
    location = zone_map.get(x, {}).get(y, {})
    description = location.get('DESCRIPTION', '')
    width = len(description) + 4
    print(f"\n{'#' * width}\n# {description} #\n{'#' * width}")
