from map import zone_map, DESCRIPTION, WHERE_AM_I

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


class Player:
    def __init__(self):
        self.name = ''
        self.clazz = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        # todo: start location should be random each game
        self.location = [1, 1]
        self.game_over = False


player = Player()


def set_class(clazz):
    player.clazz = clazz
    player.hp = valid_classes[clazz]['hp']
    player.mp = valid_classes[clazz]['mp']


def print_location():
    x, y = player.location
    location = zone_map.get(x, {}).get(y, {})
    whereami = location.get(WHERE_AM_I)
    width = len(whereami) + 4
    print(f"\n{'#' * width}\n# {whereami} #\n{'#' * width}")
