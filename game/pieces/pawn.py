from game.piece import Piece
from game.point import Point
from game.color import Color
from game.move import RegularMove, CaptureMove


class Pawn(Piece):
    _icon = '󰡙'
    _code = 6

    def get_captures(self, board):
        captures = []
        forward = self.pos + Point(0, 1 if self.color == Color.WHITE else -1)

        for dest in forward + Point(1, 0), \
                    forward + Point(-1, 0):

            if  dest.on_board() and \
                board[dest] is not None and \
                board[dest].color != self.color:

                captures.append(CaptureMove(self, dest))

        return captures

    def get_moves(self, board):
        moves = []
        step = Point(0, 1 if self.color == Color.WHITE else -1)
        dest = self.pos + step
        if dest.on_board() and board[dest] is None:
            moves.append(RegularMove(self, dest))

            at_home = self.pos.y == \
                    (1 if self.color == Color.WHITE else 6)
            dest2 = dest + step
            if  at_home and \
                dest2.on_board() and \
                board[dest2] is None:

                moves.append(RegularMove(self, dest2))

        return moves + self.get_captures(board)
