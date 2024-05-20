import tkinter as tk
import fen
from games_db import GamesDB
from app_state import GameState

class MenuActivity(tk.Frame):
    def __init__(self, app):
        super().__init__(app)

        self.app = app
        play_btn = tk.Button(self, text="Играть", command=self.play)
        play_btn.pack()
        self.db = GamesDB()

    def play(self):
        # board = fen.build()
        # game_id = self.db.reg(board)
        game_id = 1
        board = self.db.get(game_id)
        board.on_move.connect(lambda move: self.db.update(game_id, board))
        self.app.set_state(GameState(board))
