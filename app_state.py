from abc import ABC

class AppState(ABC):
    pass

class MenuState(AppState):
    pass

class GameState(AppState):
    def __init__(self, board):
        self.board = board

class ResultState(AppState):
    def __init__(self, result):
        self.result = result
