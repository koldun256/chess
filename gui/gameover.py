import tkinter as tk
from game.board import GameResult

class GameoverScreen(tk.Frame):
    def __init__(self, parent, result):
        super().__init__(parent)
        label = tk.Label(self, text="Game over(")
        label.config(font =("Courier", 14))
        label.pack()
