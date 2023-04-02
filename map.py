"""
0,1 0,2... # PLAYER STARTS AT 1,1

            OCEAN
              0   1   2   3
            ─────────────────
MOUNTAINS   │   │   │ ^ │   │ 0  HIGH CLIFF
            ─────────────────
            │ ~ │ H │ ^ │ ^ │ 1
            ─────────────────
            │ ^ │ ^ │ ^ │   │ 2
            ─────────────────
            │   │ ~ │   │   │ 3
            ─────────────────
            DESERT

Legend:
^ - Forest/Trees
~ - Lake/River
x - Island in the Ocean
H - Home

"""

ZONE_NAME = 'zone'
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False

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
    1: {
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
    2: {
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
    3: {
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
