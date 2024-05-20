import tkinter as tk
import fen
from app_state import GameState

class MenuActivity(tk.Frame):
    def __init__(self, app):
        super().__init__(app)

        self.app = app
        play_btn = tk.Button(self, text="Играть", command=self.play)
        play_btn.pack()

    def play(self):
        board = fen.build()
        self.app.set_state(GameState(board))
