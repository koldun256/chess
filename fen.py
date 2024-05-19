from game.piece import Color
from game.board import Board
from game.point import Point

from game.pieces.rook import Rook
from game.pieces.pawn import Pawn
from game.pieces.king import King
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from game.pieces.queen import Queen

notation = {
    'r': Rook,
    'n': Knight,
    'q': Queen,
    'k': King,
    'p': Pawn,
    'b': Bishop
}

def build(fen):
    piece_data = fen.split(' ')[0]
    rows = reversed(piece_data.split('/'))
    board = Board()
    
    for rowI, row in enumerate(rows):
        colI = 0
        while(colI < 8):
            for sym in row:
                if sym.isdigit():
                    colI += int(sym)
                else:
                    piece_class = notation[sym.lower()]
                    color = Color.WHITE \
                            if sym.isupper() \
                            else Color.BLACK
                    piece = piece_class(Point(colI, rowI), color)
                    board.add(piece)
                    colI += 1

    return board

