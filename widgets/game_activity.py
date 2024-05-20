import tkinter as tk
from widgets.board_widget import BoardWidget
from widgets.top_bar import TopBar
from app_state import ResultState
from game.color import Color

class GameActivity(tk.Frame):
    def __init__(self, app, board):
        super().__init__(app)
        self.board = board
        top_bar = TopBar(self, board, app)
        top_bar.pack()

        board_widget = BoardWidget(self, board)
        board_widget.pack()
        board.on_end.connect(lambda r: \
                app.set_state(ResultState(r)))

