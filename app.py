import tkinter as tk
from widgets.result_activity import ResultActivity
from widgets.game_activity import GameActivity
from widgets.menu_activity import MenuActivity
from app_state import MenuState, GameState, ResultState

class App(tk.Tk):
    activity = None
    def __init__(self):
        super().__init__()
        self.title("Chess")
        self.geometry('800x850')
        self.set_state(MenuState())

    def set_state(self, state):
        self.state = state
        self.render()

    def render(self):
        if self.activity:
            self.activity.destroy()

        if isinstance(self.state, MenuState):
            self.activity = MenuActivity(self)

        if isinstance(self.state, GameState):
            self.activity = GameActivity(self, self.state.board)

        if isinstance(self.state, ResultState):
            self.activity = ResultActivity(self, self.state.result)

        self.activity.pack()
        self.activity.place(relx=.5, rely=.5, anchor=tk.CENTER)


if __name__ == '__main__':
    app = App()
    app.mainloop()
