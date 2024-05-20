import tkinter as tk
from game.color import Color, opposite_color
from app_state import MenuState
from widgets.button import Button

class TopBar(tk.Frame):
    def __init__(self, parent, board, app):
        super().__init__(parent, height=50, width=850)
        self.board = board
        self.pack_propagate(0)
        # self.label = tk.Label(self, text="bipki", font=("ProggyClean Nerd Font", 20))
        # self.label.pack()

        board.on_move.connect(lambda move: self.set_color())
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.home_btn = Button(self, width=45, height=42, img="img/home_black.png", bg="red", command=lambda _: app.set_state(MenuState()))
        self.home_btn.pack()
        self.home_btn.place(x=75, rely=.5, anchor=tk.CENTER)

        self.set_color()

    def set_color(self):
        color = self.board.color_to_move
        self.configure(bg=color.value)
        self.home_btn.config(\
            img='img/home_black.png' if color == Color.WHITE else 'img/home_white.png', \
            bg=color.value)
