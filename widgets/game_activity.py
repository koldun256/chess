import tkinter as tk
from widgets.board_widget import BoardWidget
from app_state import ResultState

class GameActivity(tk.Frame):
    def __init__(self, app, board):
        super().__init__(app)

        board_widget = BoardWidget(self, board)
        board_widget.pack()
        board.on_end.connect(lambda r: \
                app.set_state(ResultState(r)))
