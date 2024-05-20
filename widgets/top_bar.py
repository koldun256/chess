import tkinter as tk
from game.color import Color, opposite_color
from game.board import GameStatus
from app_state import MenuState
from widgets.button import Button

result_text = {
    GameStatus.WHITE_WON: "WHITE WON",
    GameStatus.BLACK_WON: "BLACK WON",
    GameStatus.DRAW: "DRAW",
}

class TopBar(tk.Frame):
    label = None
    def __init__(self, parent, board, app):
        super().__init__(parent, height=50, width=850)
        self.board = board
        self.pack_propagate(0)

        board.on_move.connect(lambda move: self.set_color(board.color_to_move))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.home_btn = Button(self, width=45, height=42, \
            img="img/home_black.png", bg="black", \
            command=lambda _: app.set_state(MenuState()))

        self.home_btn.pack()
        self.home_btn.place(x=75, rely=.5, anchor=tk.CENTER)

        if board.status != GameStatus.ONGOING:
            self.label = tk.Label(self, text=result_text[board.status], font=("ProggyClean Nerd Font", 20))
            self.label.pack()
            self.label.place(relx=.5, rely=.5, anchor=tk.CENTER)
            self.set_color(opposite_color(board.color_to_move))
        else:
            self.set_color(board.color_to_move)

    def set_color(self, color):
        try:
            self.configure(bg=color.value)
        except:
            return

        if self.label is not None:
            self.label.configure(bg=color.value, fg=opposite_color(color).value)
        self.home_btn.config(\
            img='img/home_black.png' if color == Color.WHITE else 'img/home_white.png', \
            bg=color.value)
