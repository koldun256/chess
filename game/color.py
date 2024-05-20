from enum import Enum

class Color(Enum):
    WHITE = "#d7dbc0"
    BLACK = "#2a302a"


def opposite_color(color):
    return Color.BLACK if color == Color.WHITE else Color.WHITE
