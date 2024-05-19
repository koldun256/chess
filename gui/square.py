import tkinter as tk
from PIL import ImageTk, Image
from game.color import Color
from game.pieces.pawn import Pawn
from game.pieces.bishop import Bishop
from game.pieces.king import King
from game.pieces.queen import Queen
from game.pieces.rook import Rook
from game.pieces.knight import Knight

piece_names = {
    Pawn: "pawn",
    Bishop: "bishop",
    King: "king",
    Queen: "queen",
    Rook: "rook",
    Knight: "knight"
}

color_names = {
    Color.WHITE: "white",
    Color.BLACK: "black"
}

def load_image(piece):
    color_name = color_names[piece.color]
    piece_name = None
    for piece_class, name in piece_names.items():
        if isinstance(piece, piece_class):
            piece_name = name
    img = Image.open(f"gui/img/{color_name}_{piece_name}.png")
    new_size = (img.size[0] * 4, img.size[1] * 4)
    return ImageTk.PhotoImage(img.resize(new_size, resample=Image.NEAREST))

bg = {
    Color.WHITE: "#d7dbc0",
    Color.BLACK: "#2a302a"
}

class Square(tk.Canvas):
    def __init__(self, parent, pos, board):
        self.board = board
        self.pos = pos
        color = bg[Color.WHITE if (pos.x + pos.y) % 2 == 0 else Color.BLACK]
        tk.Canvas.__init__(self, parent, width=100, height=100, bg=color)
        board.on_move.connect(lambda p, o, d: self.render())
        self.render()


    def render(self):
        self.delete('all')
        piece = self.board[self.pos]
        if(piece is None):
            return

        self.icon = load_image(piece)
        self.create_image((50, 50), image=self.icon)
