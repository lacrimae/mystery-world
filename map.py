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


def is_solved(x, y):
    return zone_map[x][y][SOLVED]
