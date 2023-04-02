from constants import dialog
from map import zone_map, ITEMS, EXAMINATION, DESC
from models.player import player
from utils.type_util import print_slow


def examine():
    x, y = player.location
    location = zone_map.get(x, {}).get(y, {})
    items = location.get(ITEMS)

    print_slow(location.get(EXAMINATION))

    if items:
        print_slow(f'\n\nWhat would you like to examine?\n')
        print_slow(f"(You can choose {', '.join(items)})\n")

        print_item_desc(items, input('> ').lower())
    else:
        print_slow("\nThere's no available items for examination.\n\n")

    print(dialog.CONTINUE)
    input()


def print_item_desc(items, item):
    for i in items:
        if i.lower() == item:
            print_slow(items[i][DESC] + '\n\n')
            return

    print(f"Please choose a valid item. Available items for examination: {', '.join(items)}.\n")
    print_item_desc(items, input('> ').lower())
