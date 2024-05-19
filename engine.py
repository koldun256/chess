from stockfish import Stockfish

class Engine(Stockfish):
    def __init__(self, board, fen):
        super().__init__(path='/bin/stockfish')
        self.set_fen_position(fen)
        self.board = board

        board.on_move.connect( \
            lambda _, origin, dest: \
                self.make_moves_from_current_position([str(origin) + str(dest)]) \
        )


    async def best_move(self):
        return self.get_best_move(1000)
