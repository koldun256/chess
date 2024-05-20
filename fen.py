from game.piece import Color
from game.board import Board, GameStatus
from game.point import Point

from game.pieces.rook import Rook
from game.pieces.pawn import Pawn
from game.pieces.king import King, Side
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from game.pieces.queen import Queen

default_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 1'

notation = {
    'r': Rook,
    'n': Knight,
    'q': Queen,
    'k': King,
    'p': Pawn,
    'b': Bishop
}

def build(fen=default_fen):
    piece_data, color, castling, en_passant, status = fen.split(' ')
    rows = reversed(piece_data.split('/'))
    board = Board()
    board.color_to_move = Color.WHITE if color == 'w' else Color.BLACK
    
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

    board.en_passant = None if en_passant == '-' else Point.from_str(en_passant)

    board.get_king(Color.WHITE).has_castling[Side.QUEEN_SIDE] = 'Q' in castling
    board.get_king(Color.WHITE).has_castling[Side.KING_SIDE] = 'K' in castling
    board.get_king(Color.BLACK).has_castling[Side.QUEEN_SIDE] = 'q' in castling
    board.get_king(Color.BLACK).has_castling[Side.KING_SIDE] = 'k' in castling

    board.status = GameStatus(int(status))

    return board

def get_symbol(piece):
    for sym, piece_class in notation.items():
        if isinstance(piece, piece_class):
            return sym.upper() if piece.color == Color.WHITE else sym


def to_fen(board):
    matrix = board.to_matrix()
    piece_data = []
    for row in reversed(matrix):
        empty = 0
        row_data = []
        for piece in row:
            if piece is None:
                empty += 1
            else:
                if empty != 0:
                    row_data.append(str(empty))
                    empty = 0
                row_data.append(get_symbol(piece))

        if empty != 0:
            row_data.append(str(empty))

        piece_data.append(''.join(row_data))

    piece_data = '/'.join(piece_data)
    color = 'w' if board.color_to_move == Color.WHITE else 'b'
    castling = ''

    if board.get_king(Color.WHITE).has_castling[Side.KING_SIDE]:
        castling += 'K'
    if board.get_king(Color.WHITE).has_castling[Side.QUEEN_SIDE]:
        castling += 'Q'
    if board.get_king(Color.BLACK).has_castling[Side.KING_SIDE]:
        castling += 'k'
    if board.get_king(Color.BLACK).has_castling[Side.QUEEN_SIDE]:
        castling += 'q'

    if castling == '':
        castling = '-'

    en_passant = '-' if board.en_passant is None else str(board.en_passant)

    return f"{piece_data} {color} {castling} {en_passant} {board.status.value}"
