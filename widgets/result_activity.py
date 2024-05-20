import tkinter as tk
from app_state import MenuState
from game.board import GameResult

text = {
    GameResult.WHITE_WON: "Победили белые",
    GameResult.BLACK_WON: "Победили черные",
    GameResult.DRAW: "Ничья"
}

class ResultActivity(tk.Frame):
    def __init__(self, app, result):
        super().__init__(app)
        label = tk.Label(self, text=text[result])
        label.config(font =("Courier", 14))
        label.pack()
        menu_btn = tk.Button(self, text="To menu", command=lambda: app.set_state(MenuState()))
        menu_btn.pack()
