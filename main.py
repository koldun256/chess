import fen
from engine import Engine
from logger import Logger
from gui.gui import gui_loop
from game.pieces.queen import Queen
from game.point import Point
from copy import deepcopy
import asyncio


async def main():
    start_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    board = fen.build(start_fen)
    # engine = Engine(board, start_fen)
    logger = Logger(board, start_fen)

    gui_loop(board)

if __name__ == '__main__':
    asyncio.run(main())

