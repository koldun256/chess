from copy import deepcopy

from game.point import Point
from game.color import Color, opposite_color
from game.observable import Observable
from game.pieces.king import King


class InvalidMoveException(Exception):
    pass


class Board():
    _pieces = set()
    _color_to_move = Color.WHITE

    def __init__(self, pieces=None):
        self._pieces = pieces if pieces else set()
        self.on_move = Observable()


    def move(self, _str):
        origin = Point.from_str(_str[:2])
        dest = Point.from_str(_str[2:])
        piece = self[origin]

        if piece is None or piece.color != self.color_to_move:
            raise InvalidMoveException

        move = next((move for move in piece.get_moves(self) \
                    if move.dest == dest), None)

        if move is None or self.leads_to_check(move):
            raise InvalidMoveException

        move.apply(self)
        self._color_to_move = opposite_color(self.color_to_move)
        self.on_move.emit(piece, origin, piece.pos)


    def add(self, piece):
        if self[piece.pos] != None:
            raise InvalidMoveException()

        self._pieces.add(piece)


    def capture(self, pos: Point) -> None:
        self.pieces = set(p for p in self.pieces if p.pos != pos)


    def toggle_color(self):
        self._color_to_move =   Color.BLACK \
                                if self.color_to_move == Color.WHITE \
                                else Color.WHITE


    def is_attacked(self, color, pos):
        for p in self.pieces:
            if p.color == color:
                continue
            
            for move in p.get_moves(self):
                if pos == move.dest:
                    return True

        return False


    def is_color_checked(self, color):
        return self.is_attacked(color, self.get_king(color).pos)


    def get_king(self, color):
        for p in self.pieces:
            if p.color == color and isinstance(p, King):
                return p
        return None


    def leads_to_check(self, move):
        test_board = deepcopy(self)
        move.apply(test_board)
        return test_board.is_color_checked(move.piece.color)


    @property
    def color_to_move(self):
        return self._color_to_move

    
    @property
    def pieces(self):
        return self._pieces


    def to_matrix(self):
        content = [[None] * 8 for _ in range(8)]

        for p in self.pieces:
            content[p.pos.y][p.pos.x] = p

        return content


    def __getitem__(self, pos: Point):
        for p in self.pieces:
            if p.pos == pos:
                return p

        return None


    def __repr__(self):
        result = []
        matrix = self.to_matrix()
        for row in reversed(matrix):
            result.append(''.join(map( \
                lambda p: p.icon if p is not None else '.', \
                row \
            )))

        return '\n'.join(result)
