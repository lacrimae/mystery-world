from src.constants import dialog
from src.models.map import zone_map, DESC
from src.models.player import player
from src.utils.type_util import print_slow


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
    print_slow(zone_map[new_x][new_y][DESC] + '\n')
    player.location = [new_x, new_y]
