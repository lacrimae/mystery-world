from src.constants import dialog
from src.model.map import zone_map, ITEMS, CAN_BE_TAKEN, EXAMINATION
from src.model.player import player
from src.utils.type_util import print_slow


def take():
    x, y = player.location
    location = zone_map.get(x, {}).get(y, {})
    items = location.get(ITEMS)
    items_can_be_taken = [item.lower() for item in items.keys() if
                          items[item][CAN_BE_TAKEN] and item not in player.inventory]

    print_slow(location.get(EXAMINATION))

    if items_can_be_taken:
        print_slow(f'\nWhat would you like to pick up?\n')
        print_slow(f"(You can take {', '.join(items_can_be_taken).capitalize()})\n")

        take_item(items_can_be_taken)
    else:
        print_slow("\nThere are no items that can be taken at the moment.\n\n")

    print(dialog.CONTINUE)
    input()


def take_item(items):
    item = input('> ').lower()
    if item in items:
        player.inventory.append(item.capitalize())
        print_slow(f'You have taken {item.capitalize()}.\n\n')
    else:
        print(f"Please choose a valid item. Available items that can be taken: {', '.join(items)}.\n")
        take_item(items)
