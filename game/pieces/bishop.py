from game.piece import Piece
from game.point import Point
from game.move import RegularMove, CaptureMove


class Bishop(Piece):
    _icon = '󰡜'
    _code = 3

    def get_moves(self, board):
        moves = []
        for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            step = Point(dx, dy)
            dest = self._pos + step

            while dest.on_board() and board[dest] is None:
                moves.append(RegularMove(self, dest))
                dest += step

            if dest.on_board() and board[dest].color != self.color:
                moves.append(CaptureMove(self, dest))

        return moves
