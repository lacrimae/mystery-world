from src.model.map import zone_map, WHERE_AM_I

VALID_CLASSES = {
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
    }
}


class Player:
    def __init__(self):
        self.name = ''
        self.clazz = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.inventory = []
        self.location = [1, 1]
        self.game_over = False

    def set_class(self, clazz):
        self.clazz = clazz
        self.hp = VALID_CLASSES[clazz]['hp']
        self.mp = VALID_CLASSES[clazz]['mp']

    def print_location(self):
        x, y = self.location
        location = zone_map.get(x, {}).get(y, {})
        whereami = location.get(WHERE_AM_I)
        width = len(whereami) + 4
        print(f"\n{'#' * width}\n# {whereami} #\n{'#' * width}")

    def open_inventory(self):
        if self.inventory:
            items = ', '.join(self.inventory)
            print(f"You have the following items in your bags: {items}.")
        else:
            print('Your bags are empty.')


player = Player()
