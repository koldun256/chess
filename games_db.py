import sqlite3
from fen import build, to_fen

class GamesDB:
    def __init__(self):
        self.conn = sqlite3.connect('games.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS games(
           game_id INTEGER PRIMARY KEY AUTOINCREMENT,
           fen TEXT
        );""")

    def list(self):
        self.cur.execute('SELECT game_id FROM games')
        return self.cur.fetchall()

    def get(self, game_id):
        self.cur.execute('SELECT * FROM games WHERE game_id=?', (game_id, ))
        return build(self.cur.fetchone()[1])

    def reg(self, board):
        self.cur.execute(f'INSERT INTO games (fen) VALUES ("{to_fen(board)}");')
        self.conn.commit()
        return self.cur.lastrowid

    def update(self, game_id, board):
        self.cur.execute(f'UPDATE games SET fen="{to_fen(board)}" WHERE game_id={game_id};')
        self.conn.commit()

