import tkinter as tk
from widgets.square import Square
from game.color import Color
from game.point import Point
from game.board import InvalidMoveException, GameStatus
from observable import Observable


class BoardWidget(tk.Frame):
    selected_sqare = None
    possible_moves = []
    
    def __init__(self, parent, board):
        tk.Frame.__init__(self, parent, highlightthickness=0)
        self.board = board
        self.on_select = Observable()

        for row in range(8):
            for col in range(8):
                point = Point(col, row)
                square = Square(self, point, board)
                square.grid(row=7-row, column=col)

                if board.status == GameStatus.ONGOING:
                    square.bind("<Button-1>", lambda _, p=point: self.select(p))

    def select(self, point):
        moved = False
        if self.selected_sqare is not None:
            try:
                self.board.move(self.selected_sqare, point)
                moved = True
            except InvalidMoveException:
                pass
            self.selected_sqare = None
            self.possible_moves = []

        if self.selected_sqare is None and not moved:
            piece = self.board[point]
            if piece is not None and piece.color == self.board.color_to_move:
                self.selected_sqare = piece.pos
                self.possible_moves = piece.get_moves(self.board)

        self.on_select.emit(point)
