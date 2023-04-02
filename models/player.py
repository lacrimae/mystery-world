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
