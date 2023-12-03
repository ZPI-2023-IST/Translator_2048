from enum import Enum


class State(Enum):
    ONGOING = 'ONGOING'
    WON = 'WON'
    LOST = 'LOST'


class MOVES(Enum):
    UP = ('w', [1, 0, 0, 0])
    DOWN = ('s', [0, 1, 0, 0])
    LEFT = ('a', [0, 0, 1, 0])
    RIGHT = ('d', [0, 0, 0, 1])


FIELDS_VALUES = \
    {None: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     2: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     4: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     8: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     16: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     32: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     64: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     128: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     256: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     512: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     1024: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     2048: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}

def get_enum_member(value):
    for member in MOVES:
        if member.value[0] == value:
            return member
    raise ValueError(f"No Enum member with value '{value}' found")