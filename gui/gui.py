import tkinter as tk
from gui.square import Square
from game.color import Color
from game.point import Point

class Board:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.create_board()

    def create_board(self):
        for row in range(8):
            for col in range(8):
                square = Square(self.root, Point(col, row))
                square.grid(row=row, column=col)

def gui_loop():
    root = tk.Tk()
    game = Board(root)
    root.mainloop()
