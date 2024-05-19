import tkinter as tk

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.create_board()

    def create_board(self):
        for row in range(8):
            for col in range(8):
                square_color = "white" if (row + col) % 2 == 0 else "black"
                square = tk.Button(self.root, bg=square_color, width=5, height=2)
                square.grid(row=row, column=col)

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()
