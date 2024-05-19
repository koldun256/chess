import tkinter as tk
from game.color import Color

bg = {
    Color.WHITE: "#d7dbc0",
    Color.BLACK: "#2a302a"
}

class Square(tk.Frame):
    def __init__(self, parent, pos):
        color = Color.WHITE if (pos.x + pos.y) % 2 == 0 else Color.BLACK
        tk.Frame.__init__(self, parent, width=100, height=100, bg=bg[color])
