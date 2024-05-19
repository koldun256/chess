from game.piece import Piece
from game.point import Point
from game.move import RegularMove, CaptureMove
from game.pieces.king import BreakCastlingMove, Side


class Rook(Piece):
    _icon = '󰡛'


    def __init__(self, pos, color):
        self._side = Side.QUEEN_SIDE if pos.x == 0 else Side.KING_SIDE
        super().__init__(pos, color)


    def get_moves(self, board):
        moves = []
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            step = Point(dx, dy)
            dest = self._pos + step

            while dest.on_board() and board[dest] is None:
                moves.append(RegularMove(self, dest))
                dest += step

            if dest.on_board() and board[dest].color != self.color:
                moves.append(CaptureMove(self, dest))

        return [BreakCastlingMove(move, (self._side)) \
                for move in moves]
