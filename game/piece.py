from abc import ABC, abstractmethod
from game.color import Color


class Piece(ABC):
    def __init__(self, pos, color):
        self._pos = pos
        self._color = color


    @abstractmethod
    def get_moves(self):
        pass


    @property
    def icon(self):
        if self.color == Color.WHITE:
            return self._icon
        return f'\x1b[1;32m{self._icon}\x1b[0m'


    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, val):
        self._pos = val

    @property
    def color(self):
        return self._color


    def __hash__(self):
        return hash(self.pos)


    def __repr__(self):
        c = 'w' if self.color == Color.WHITE else 'b'
        return f'{c}{self.icon}{self.pos}'
