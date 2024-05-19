import tkinter as tk
from gui.square import Square
from game.color import Color
from game.point import Point

class Board:
    def __init__(self, root, board):
        self.root = root
        self.root.title("Chess Game")
        self.create_board(board)

    def create_board(self, board):
        for row in range(8):
            for col in range(8):
                square = Square(self.root, Point(col, row), board)
                square.grid(row=7-row, column=col)

def gui_loop(board):
    root = tk.Tk()
    game = Board(root, board)
    root.mainloop()
