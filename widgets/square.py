import tkinter as tk
from PIL import ImageTk, Image
from game.move import RegularMove, CaptureMove
from game.color import Color, opposite_color
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
    img = Image.open(f"img/{color_name}_{piece_name}.png")
    new_size = (img.size[0] * 4, img.size[1] * 4)
    return ImageTk.PhotoImage(img.resize(new_size, resample=Image.NEAREST))

class Square(tk.Canvas):
    def __init__(self, parent, pos, board):
        self.board = board
        self.pos = pos
        self.parent = parent
        self.color = Color.WHITE if (pos.x + pos.y) % 2 == 0 else Color.BLACK
        super().__init__(parent, width=100, height=100, bg=self.color.value, highlightthickness=0)
        parent.on_select.connect(lambda p: self.render())
        self.render()


    def render(self):
        try:
            self.delete('all')
        except:
            return
        piece = self.board[self.pos]

        if(piece is not None):
            self.icon = load_image(piece)
            self.create_image((50, 50), image=self.icon)

        if(self.pos == self.parent.selected_sqare):
            self.create_rectangle(7, 7, 93, 93, outline=opposite_color(self.color).value, width=4, dash=(10, 10))

        move = next((move for move in self.parent.possible_moves if move.dest == self.pos), None)

        if move is None:
            return

        if move.is_capture:
            self.create_rectangle(7, 7, 93, 93, outline=opposite_color(self.color).value, width=7)
        else:
            self.create_rectangle(45, 45, 55, 55, fill=opposite_color(self.color).value)

