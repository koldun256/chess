from string import ascii_lowercase
import copy

class Point():
    @staticmethod
    def from_str(_str):
        return Point(   ascii_lowercase.find(_str[0]), \
                        int(_str[1]) - 1)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def on_board(self):
        return 0 <= self.x < 8 and 0 <= self.y < 8


    def __repr__(self):
        return f'{ascii_lowercase[self.x]}{self.y + 1}'


    def __hash__(self):
        return self.x * 8 + self.y

    def __copy__(self):
        return Point(self.x, self.y)
