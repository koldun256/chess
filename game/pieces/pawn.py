from game.piece import Piece
from game.point import Point
from game.color import Color
from game.move import RegularMove, CaptureMove, Move
from game.pieces.queen import Queen

class EnPassantMove(Move):
    is_capture = True
    def __init__(self, piece, dest):
        self._piece = piece
        self._dest = dest

    def apply(self, board):
        board.capture(Point(self.dest.x, self.dest.y + \
                (1 if self.color == Color.BLACK else -1)))
        board[self.piece.pos].pos = self.dest

class TransformMove(Move):
    is_capture = False
    def __init__(self, base_move):
        self._piece = base_move.piece
        self._dest = base_move.dest
        self.is_capture = base_move.is_capture
        self.base_move = base_move

    def apply(self, board):
        self.base_move.apply(board)
        board.capture(self.dest)
        board.add(Queen(self.dest, self.piece.color))

class JumpMove(RegularMove):
    def apply(self, board):
        super().apply(board)
        board.en_passant = self.dest + Point(0, \
                -1 if self.color == Color.WHITE else 1)

class Pawn(Piece):
    _icon = '󰡙'
    _code = 1

    def get_captures(self, board):
        captures = []
        forward = self.pos + Point(0, 1 if self.color == Color.WHITE else -1)

        for dest in forward + Point(1, 0), \
                    forward + Point(-1, 0):

            if  dest.on_board() and \
                board[dest] is not None and \
                board[dest].color != self.color:

                captures.append(CaptureMove(self, dest))

            if dest == board.en_passant:
                captures.append(EnPassantMove(self, dest))

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

                moves.append(JumpMove(self, dest2))

        return [TransformMove(move) \
                if move.dest.y == 0 or move.dest.y == 7 \
                else move \
                for move in moves + self.get_captures(board) \
                if not board.leads_to_check(move)]
