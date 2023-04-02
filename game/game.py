from constants import dialog
from models.player import player
from utils.type_util import print_slow
from map import zone_map

import os
import sys

available_actions = {
    'QUIT': 'quit',
    'MOVE': ['move', 'go', 'travel', 'walk'],
    'EXAMINE': ['examine', 'look', 'inspect'],
    'TAKE': ['take', 'interact']
}


def start_game():
    setup()
    play()


def setup():
    os.system('clear')

    # NAME
    print_slow(dialog.FIRST_SCENE_1)
    player.name = input('> ')

    # CLASS
    valid_classes = {
        'warrior': {
            'hp': 150,
            'mp': 0
        },
        'rogue': {
            'hp': 100,
            'mp': 50
        },
        'mage': {
            'hp': 50,
            'mp': 100
        }}

    print_slow(dialog.FIRST_SCENE_2.format(player.name))
    print(dialog.FIRST_SCENE_2_1)
    player_clazz = input('> ')
    while player_clazz.lower() not in valid_classes:
        print(f"Please choose one of the following classes: {', '.join(valid_classes)}")
        player_clazz = input('> ')

    player.clazz = player_clazz
    player.hp = valid_classes[player_clazz]['hp']
    player.mp = valid_classes[player_clazz]['mp']

    question3 = f"A noble choice! You are now a {player_clazz.capitalize()}!\n"
    print_slow(question3)

    print("Press the 'Enter' key to return to the main menu.")
    input()

    os.system('clear')
    print("####################")
    print("# Let's start now! #")
    print("####################")


def play():
    while player.game_over is False:
        prompt()


def prompt():
    print('\n' + '──────────────────────────────────')
    print('What would you like to do?')
    action = input('> ')
    # available_actions = ['move', 'quit', 'examine', 'take']

    while not any(action.lower() in actions for actions in available_actions.values()):
        print('Unknown action, try again.\n')
        action = input('> ')

    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in available_actions['MOVE']:
        move()
    # elif action.lower() in available_actions['EXAMINE']:
    # examine()
    # elif action.lower() in available_actions['TAKE']:
    #     take()


def move():
    direction = input("Where would you like to move? ").lower().strip()

    y, x = player.location

    if direction == "up" and y == 0:
        print(
            "Before you lies an infinite ocean, stretching out to the horizon as far as the eye can see. The "
            "waters beckon you to venture forth, but know that to do so is to embrace the possibility of death.")
    elif direction == "down" and y == len(zone_map) - 1:
        print(
            "Before you stretches a seemingly endless expanse of desert, with dunes rising and falling like waves "
            "on an ocean of sand. Though the path ahead is treacherous and fraught with danger, the temptation to "
            "press onward and uncover the secrets of this desolate place beckons you ever forward.")
    elif direction == "left" and x == 0:
        print(
            "Before you tower the endless peaks of a majestic mountain range, their snow-capped summits piercing "
            "the very heavens. The urge to explore their heights is irresistible, but you know that with every "
            "step you take, you risk succumbing to the perils of this harsh and unforgiving terrain.")
    elif direction == "right" and x == len(zone_map[y]) - 1:
        print(
            "Before you looms a towering cliff, its sheer face rising steeply into the clouds above. The drop is "
            "dizzying, and the risk of a misstep or a sudden gust of wind is ever present. Beyond the edge lies a "
            "world of mystery and adventure, but know that to take the leap is to embrace certain death.")
    else:
        if direction == "up":
            print("You have moved North.")
            player.location[y] -= 1
        elif direction == "down":
            print("You have moved South.")
            player.location[y] += 1
        elif direction == "left":
            print("You have moved West.")
            player.location[x] -= 1
        elif direction == "right":
            print("You have moved East.")
            player.location[x] += 1
        else:
            print("Invalid direction.")


def print_location():
    x, y = player.location
    location = zone_map.get(x, {}).get(y, {})
    description = location.get('DESCRIPTION', '')
    width = len(description) + 4
    print(f"\n{'#' * width}\n# {description} #\n{'#' * width}")
