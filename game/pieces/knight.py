from game.piece import Piece
from game.point import Point
from game.move import RegularMove, CaptureMove


class Knight(Piece):
    _icon = '󰡘'
    _code = 2

    def get_moves(self, board):
        moves = []
        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1),\
                       (1, 2), (1, -2), (-1, 2), (-1, -2)]:

            dest = self._pos + Point(dx, dy)
            if not dest.on_board():
                continue

            if board[dest] is None:
                moves.append(RegularMove(self, dest))
                continue

            if board[dest].color != self.color:
                moves.append(CaptureMove(self, dest))

        return moves
