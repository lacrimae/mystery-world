import cmd
import textwrap
import os
import sys
import time

screen_width = 100

""" Player Setup """


class player:
    def __init__(self):
        self.name = ''
        self.clazz = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = [0, 1]
        self.game_over = False


player = player()

""" Title Screen """


def title_screen_selections():
    option = input("> ")
    select_option(option)
    while True:
        if option.lower() == 'play':
            start_game()
            break
        elif option.lower() == 'help':
            help_menu()
            break
        elif option.lower() == 'quit':
            sys.exit()
        else:
            print("Please choose 'play', 'help', or 'quit' ≖‿≖")
            option = input("> ")


def select_option(option):
    if option.lower() == ("play"):
        start_game()  # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()


def help_menu():
    print('################################')
    print('# Welcome to the Mystery Game! #')
    print('################################')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "examine" to inspect something')
    print('- Use "take" to put item in a bag')
    print('- Good luck and have fun!')
    title_screen_selections()


def title_screen():
    os.system('clear')
    print('################################')
    print('# Welcome to the Mystery Game! #')
    print('################################')
    print('            - Play -            ')
    print('            - Help -            ')
    print('            - Quit -            ')
    title_screen_selections()


# GAME INTERACTIVITY #
def print_location():
    x, y = player.location
    location = zone_map.get(x, {}).get(y, {})
    description = location.get('DESCRIPTION', '')
    width = len(description) + 4
    print(f"\n{'#' * width}\n# {description} #\n{'#' * width}")


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
    elif action.lower() in available_actions['EXAMINE']:
        examine()
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


def examine():
    y, x = player.location
    if zone_map[x][y][SOLVED]:
        print("You have already exhausted this zone.")
    else:
        print("You can trigger a puzzle here!")


# def take():


# GAME FUNCTIONALITY #
def start_game():
    print_location()
    print('starting..')


def main_game_loop():
    # here handle if puzzles have been solved, boss defeated, explored everything, etc.
    while player.game_over is False:
        prompt()


def setup_game():
    os.system('clear')

    # NAME
    question1 = "Greetings, traveler. I am the guildmaster, and I welcome you to our humble establishment. May I " \
                "inquire as to your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
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
    question2 = f"And what class do you seek to pursue, {player.name}? We offer three paths to glory: the brave and " \
                f"sturdy warrior, the cunning and agile rogue, and the wise and powerful mage."
    question2added = f"(You can play as a {', '.join(valid_classes)})"
    for character in question2 + question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05 if character != ")" else 0.01)
    player_clazz = input('> ')
    while player_clazz.lower() not in valid_classes:
        player_clazz = input('> ')

    player.clazz = player_clazz
    player.hp = valid_classes[player_clazz]['hp']
    player.mp = valid_classes[player_clazz]['mp']

    print(f"A noble choice! You are now a {player_clazz.capitalize()}!\n")

    os.system('clear')
    print("####################")
    print("# Let's start now! #")
    print("####################")


# ACTIONS #

available_actions = {
    'QUIT': 'quit',
    'MOVE': ['move', 'go', 'travel', 'walk'],
    'EXAMINE': ['examine', 'look', 'inspect'],
    'TAKE': ['take', 'interact']
}

# MAP #

"""
0,1 0,2... # PLAYER STARTS AT 1,1

            OCEAN
            ─────────────────
MOUNTAINS   │   │   │   │   │ 0,3  HIGH CLIFF
            ─────────────────
            │   │ x │   │   │ 1,3
            ─────────────────
            │   │   │   │   │ 2,3...
            ─────────────────
            │   │   │   │   │
            ─────────────────
            DESERT
            """
ZONE_NAME = 'zone'
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = ['up', 'north']
DOWN = ['down', 'south']
LEFT = ['left', 'west']
RIGHT = ['right', 'east']

solved_places = [[False, False, False, False],
                 [False, False, False, False],
                 [False, False, False, False],
                 [False, False, False, False]]

zone_map = {
    0: {
        0: {
            ZONE_NAME: 'Home',
            DESCRIPTION: 'description',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        1: {
            ZONE_NAME: 'Home',
            DESCRIPTION: 'description',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        2: {
            ZONE_NAME: 'Home',
            DESCRIPTION: 'description',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        3: {
            ZONE_NAME: 'Home',
            DESCRIPTION: 'description',
            EXAMINATION: 'examine',
            SOLVED: False
        },
    },
}

title_screen()
