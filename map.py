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

ZONE_NAME = 'ZONE'
WHERE_AM_I = 'WHEREAMI'
DESC = 'DESC'
EXAMINATION = 'EXAMINE'
ITEMS = 'ITEMS'
ITEM_NAME = 'ITEM_NAME'
ITEM_DESC = 'ITEM_DESC'
SOLVED = False

solved_places = [[False, False, False, False],
                 [False, False, False, False],
                 [False, False, False, False],
                 [False, False, False, False]]

zone_map = {
    0: {
        0: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        1: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        2: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        3: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
    },
    1: {
        0: {
            ZONE_NAME: 'Home',
            DESC: "",
            EXAMINATION: 'examine',
            SOLVED: False
        },
        1: {
            ZONE_NAME: 'Home',
            WHERE_AM_I: "You have arrived at the dwelling place that you call Home.",
            DESC: "You step through the front door of your small, cozy wooden house and are greeted by the "
                  "warm glow of the fireplace. The walls are lined with shelves, filled with books and "
                  "trinkets that you've collected over the years. A plush armchair sits in front of the fire, "
                  "inviting you to sit and relax. The scent of freshly baked bread and the sound of boiling "
                  "water on the stove waft through the air. You can hear the soft patter of raindrops against "
                  "the windows, and the gentle rustling of leaves in the surrounding forest. It's a peaceful "
                  "and comforting space, the perfect retreat from the outside world.",
            EXAMINATION: 'You are standing in a light room, and you can see a bed and a lamp.',
            # ITEMS: {
            #     'Bed': {
            #         DESC: "The bed is the centerpiece of the cozy bedroom, and it looks incredibly comfortable. "
            #               "The mattress is thick and plush, with fluffy white pillows and a warm, cozy duvet. "
            #               "The headboard is made of polished wood, and there are soft, comfortable blankets "
            #               "draped over the foot of the bed. A small reading lamp is perched on the nightstand "
            #               "next to the bed, casting a warm glow over the area. You can't resist the urge to "
            #               "crawl under the covers and sink into the softness of the mattress."
            #     },
            #     'Lamp': {
            #         DESC: "The lamp is small but stylish, with a sleek silver base and a frosted glass shade. It "
            #               "emits a warm and inviting light, casting a soft glow around the room. Its intricate "
            #               "etchings and delicate curves make it clear that this is not just any ordinary lamp, "
            #               "but a carefully crafted work of art."
            #     }
            # },
            SOLVED: False
        },
        2: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        3: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
    },
    2: {
        0: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        1: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        2: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        3: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
    },
    3: {
        0: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        1: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        2: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
        3: {
            ZONE_NAME: 'Home',
            DESC: 'DESC',
            EXAMINATION: 'examine',
            SOLVED: False
        },
    },
}


def is_solved(x, y):
    return zone_map[x][y][SOLVED]
