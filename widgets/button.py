import tkinter as tk
from PIL import ImageTk, Image


class Button(tk.Canvas):
    def __init__(self, parent, command, img, width, height, bg):
        super().__init__(parent, width=width, height=height, bg=bg, highlightthickness=0)
        self.width = width
        self.height = height
        self.bind("<Button-1>", command)
        self.config(img, bg)

    def config(self, img, bg):
        self.configure(bg=bg)
        self.delete('all')
        self.p_img = ImageTk.PhotoImage(\
            Image.open(img).resize((self.width, self.height),\
            resample=Image.NEAREST)\
        )
        self.create_image((self.width/2, self.height/2), image=self.p_img)
