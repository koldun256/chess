from copy import deepcopy

from game.point import Point
from game.color import Color, opposite_color
from observable import Observable
from game.pieces.king import King, CastleMove
from enum import Enum

class GameResult(Enum):
    WHITE_WON = 1
    BLACK_WON = 2
    DRAW = 3

class InvalidMoveException(Exception):
    pass


class Board():
    _pieces = set()
    color_to_move = Color.WHITE
    finished = False
    result = None
    en_passant = None

    def __init__(self, pieces=None):
        self._pieces = pieces if pieces else set()
        self.on_move = Observable()
        self.on_end = Observable()
        self.on_move.connect(lambda move: self.toggle_color())
        self.on_move.connect(lambda move: self.check_checkmate())
        self.on_move.connect(lambda move: self.check_stalemate())
        self.on_end.connect(self.set_finished)


    def move(self, *args):
        if self.finished:
            print('после драки кулаками не машут')
            return

        if len(args) == 1:
            origin = Point.from_str(args[0][:2])
            dest = Point.from_str(args[0][2:])
        else:
            origin = args[0]
            dest = args[1]


        piece = self[origin]

        if piece is None or piece.color != self.color_to_move:
            raise InvalidMoveException

        move = next((move for move in piece.get_moves(self) \
                    if move.dest == dest), None)

        if move is None or self.leads_to_check(move):
            raise InvalidMoveException
        
        self.en_passant = None
        move.apply(self)
        self.on_move.emit(move)

    def set_finished(self, result):
        self.finished = True
        self.result = result

    def check_checkmate(self):
        if self.is_checkmate():
            self.on_end.emit(   GameResult.BLACK_WON \
                                if self.color_to_move == Color.WHITE \
                                else GameResult.WHITE_WON)
    def check_stalemate(self):
        if self.is_stalemate():
            self.on_end.emit(GameResult.DRAW)

    def toggle_color(self):
        self.color_to_move = opposite_color(self.color_to_move)

    def add(self, piece):
        if self[piece.pos] != None:
            raise InvalidMoveException()

        self._pieces.add(piece)


    def capture(self, pos: Point) -> None:
        self._pieces = set(p for p in self.pieces if p.pos != pos)


    def is_attacked(self, color, pos):
        for p in self.pieces:
            if p.color == color:
                continue
            
            for move in p.get_captures(self):
                if pos == move.dest:
                    return True

        return False

    def is_stalemate(self):
        for piece in self.pieces:
            if piece.color != self.color_to_move:
                continue
            for move in piece.get_moves(self):
                return False
        return not self.is_color_checked(self.color_to_move)

    def is_checkmate(self):
        for piece in self.pieces:
            if piece.color != self.color_to_move:
                continue
            for move in piece.get_moves(self):
                return False
        return self.is_color_checked(self.color_to_move)

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
