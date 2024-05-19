from game.piece import Piece
from game.point import Point
from game.move import RegularMove, CaptureMove


class Bishop(Piece):
    _icon = '󰡜'
    _code = 3

    def get_captures(self, board):
        captures = []
        for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            step = Point(dx, dy)
            dest = self._pos + step

            while dest.on_board() and board[dest] is None:
                dest += step

            if dest.on_board() and board[dest].color != self.color:
                captures.append(CaptureMove(self, dest))

        return captures

    def get_moves(self, board):
        moves = []
        for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            step = Point(dx, dy)
            dest = self._pos + step

            while dest.on_board() and board[dest] is None:
                moves.append(RegularMove(self, dest))
                dest += step

        return [move for move in moves + self.get_captures(board) \
                if not board.leads_to_check(move)]
