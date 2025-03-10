from game.piece import Piece
from game.point import Point
from game.move import RegularMove, CaptureMove


class Knight(Piece):
    _icon = '󰡘'
    _code = 2
    def get_captures(self, board):
        captures = []
        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1),\
                       (1, 2), (1, -2), (-1, 2), (-1, -2)]:

            dest = self._pos + Point(dx, dy)
            if not dest.on_board() or board[dest] is None:
                continue

            if board[dest].color != self.color:
                captures.append(CaptureMove(self, dest))

        return captures

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

        return [move for move in moves + self.get_captures(board) \
                if not board.leads_to_check(move)]

