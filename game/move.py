from abc import ABC, abstractmethod
from game.point import Point


class Move(ABC):
    @abstractmethod
    def apply(self, board_state):
        pass


    @property
    def piece(self):
        return self._piece


    @property
    def dest(self) -> Point:
        return self._dest

    @property
    def color(self):
        return self.piece.color


class RegularMove(Move):
    is_capture = False
    def __init__(self, piece, dest):
        self._piece = piece
        self._dest = dest


    def apply(self, board):
        board[self.piece.pos].pos = self.dest


class CaptureMove(Move):
    is_capture = True
    def __init__(self, piece, dest):
        self._piece = piece
        self._dest = dest


    def apply(self, board):
        board.capture(self.dest)
        board[self.piece.pos].pos = self.dest
