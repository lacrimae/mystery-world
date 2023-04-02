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
        self.location = [0, 1]
        self.game_over = False


player = Player()


def set_class(clazz):
    player.clazz = clazz
    player.hp = valid_classes[clazz]['hp']
    player.mp = valid_classes[clazz]['mp']
