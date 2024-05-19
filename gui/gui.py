import tkinter as tk
from gui.square import Square
from game.color import Color
from game.point import Point
from game.board import InvalidMoveException
from game.observable import Observable

class BoardWidget(tk.Frame):
    selected_sqare = None
    possible_moves = []
    
    def __init__(self, parent, board):
        tk.Frame.__init__(self, parent)
        self.board = board
        self.on_select = Observable()

        for row in range(8):
            for col in range(8):
                point = Point(col, row)
                square = Square(self, point, board)
                square.grid(row=7-row, column=col)
                square.bind("<Button-1>", lambda _, p=point: self.select(p))

    def select(self, point):
        if self.selected_sqare is None:
            piece = self.board[point]
            if piece is None:
                return

            self.selected_sqare = piece.pos
            self.possible_moves = piece.get_moves(self.board)
        else:
            try:
                self.board.move(self.selected_sqare, point)
            except InvalidMoveException:
                pass

            self.selected_sqare = None
            self.possible_moves = []

        self.on_select.emit(point)

def gui_loop(board):
    root = tk.Tk()
    root.title("Chess")
    board_widget = BoardWidget(root, board)
    board_widget.pack()
    root.mainloop()
