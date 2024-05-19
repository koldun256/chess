import tkinter as tk
from gui.square import Square
from game.color import Color
from game.point import Point
from game.board import InvalidMoveException

class Board:
    selected = None
    def __init__(self, root, board):
        self.root = root
        self.root.title("Chess Game")
        self.create_board(board)
        self.board = board

    def create_board(self, board):
        for row in range(8):
            for col in range(8):
                point = Point(col, row)
                square = Square(self.root, point, board)
                square.grid(row=7-row, column=col)
                square.bind("<Button-1>", lambda _, p=point: self.select(p))

    def select(self, point):
        if self.selected is None:
            self.selected = point
            return
        try:
            self.board.move(self.selected, point)
            self.selected = None
        except InvalidMoveException:
            print('invalid move!')
def gui_loop(board):
    root = tk.Tk()
    game = Board(root, board)
    root.mainloop()
