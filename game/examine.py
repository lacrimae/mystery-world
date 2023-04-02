from constants import dialog
from map import zone_map, ITEMS, ITEM_NAME, EXAMINATION, ITEM_DESC
from models.player import player
from utils.type_util import print_slow


def examine():
    x, y = player.location
    location = zone_map.get(x, {}).get(y, {})
    items = location.get(ITEMS)
    item_names = [item[ITEM_NAME] for item in items.values()]

    print_slow(location.get(EXAMINATION))

    if items:
        print_slow(f'\n\nWhat would you like to examine?\n')
        print_slow(f"(You can choose {', '.join(item_names)})\n")

        print_item_desc(items, item_names, input('> ').lower())
    else:
        print_slow("\nThere's no available items for examination.\n")

    print_slow(dialog.CONTINUE)
    input()


def print_item_desc(items, item_names, item):
    for i in items.values():
        if i[ITEM_NAME].lower() == item:
            item_desc = i[ITEM_DESC]
            print_slow(item_desc + '\n\n')
            return

    print(f"Please choose a valid item. Available items for examination: {', '.join(item_names)}.\n")
    print_item_desc(items, item_names, input('> ').lower())
