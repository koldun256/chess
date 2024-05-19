import sqlite3

class Logger:
    def __init__(self, board, start_fen):
        self.conn = sqlite3.connect('logger.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS boards(
           board_id INT PRIMARY KEY,
           start_fen TEXT
        );""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS moves(
           move_id INT PRIMARY KEY,
           board_id TEXT,
           piece INT,
           origin INT,
           dest INT
        );""")


        self.cur.execute(f"INSERT INTO boards (start_fen) VALUES ('{start_fen}');")

        self.id = self.cur.lastrowid
        self.conn.commit()
        board.on_move.connect(lambda *args: self.log_move(*args))


    def log_move(self, piece, origin, dest):
        self.cur.execute(f"INSERT INTO moves (board_id, piece, origin, dest) VALUES (?, ?, ?, ?);", [self.id, piece._code, hash(origin), hash(dest)])
        self.conn.commit()

