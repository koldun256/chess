from enum import Enum

from game.piece import Piece
from game.point import Point
from game.move import RegularMove, CaptureMove, Move


class Side(Enum):
    KING_SIDE = 1
    QUEEN_SIDE = 2


class BreakCastlingMove(Move):
    def __init__(self, base_move, sides):
        self._base_move = base_move
        self._dest = base_move.dest
        self._piece = base_move.piece
        self._sides = sides


    def apply(self, board):
        king = board.get_king(self.piece.color)
        for side in self._sides:
            king.has_castling[side] = False
        self._base_move.apply(board)


class CastleMove(Move):
    def __init__(self, piece, side):
        self._piece = piece
        self._side = side
        self._dest = Point( 2 if side == Side.QUEEN_SIDE else 6, \
                            piece.pos.y)


    def apply(self, board):
        rook = board[Point( 0 if self._side == Side.QUEEN_SIDE else 7,
                            self.piece.pos.y)]

        rook.pos = Point(   3 if self._side == Side.QUEEN_SIDE else 5, \
                            self.piece.pos.y)

        board[self.piece.pos].pos = self.dest


class King(Piece):
    _icon = '󰡗'
    _code = 4
    def __init__(self, pos, color):
        super().__init__(pos, color)
        self.has_castling = {
            Side.KING_SIDE: True,
            Side.QUEEN_SIDE: True
        }


    def can_castle(self, board, side):
        if not self.has_castling[side]:
            return False

        busy_offs = [Point(-1, 0), Point(-2, 0), Point(-3, 0)] \
                    if side == Side.QUEEN_SIDE \
                    else [Point(1, 0), Point(2, 0)]

        for d in busy_offs:
            if board[self.pos + d]:
                return False

        att_offs =  [Point(0, 0), Point(-1, 0), Point(-2, 0)] \
                    if side == Side.QUEEN_SIDE \
                    else [Point(0, 0), Point(1, 0), Point(2, 0)]

        for d in att_offs:
            if board.is_attacked(self.color, self.pos + d):
                return False

        return True

    def get_captures(self, board):
        captures = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),\
                       (1, 1), (1, -1), (-1, 1), (-1, -1)]:

            dest = self._pos + Point(dx, dy)
            if not dest.on_board():
                continue

            if board[dest] != None and board[dest].color != self.color:
                moves.append(CaptureMove(self, dest))

        return captures

    def get_moves(self, board):
        moves = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),\
                       (1, 1), (1, -1), (-1, 1), (-1, -1)]:

            dest = self._pos + Point(dx, dy)
            if not dest.on_board():
                continue

            if board[dest] is None:
                moves.append(RegularMove(self, dest))
                continue

        moves += self.get_captures(board)

        if self.can_castle(board, Side.QUEEN_SIDE):
            moves.append(CastleMove(self, Side.QUEEN_SIDE))

        if self.can_castle(board, Side.KING_SIDE):
            moves.append(CastleMove(self, Side.KING_SIDE))

        return [BreakCastlingMove(move, (Side.KING_SIDE, Side.QUEEN_SIDE))\
                for move in moves]
