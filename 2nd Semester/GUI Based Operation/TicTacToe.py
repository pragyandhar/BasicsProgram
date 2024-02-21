import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("400x400")
        self.current_player = "X"
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self, text="", font=("Arial", 25), fg = "white", bg='Red', activebackground='Cyan',activeforeground='Blue', width=6, height=2,command=lambda i=i, j=j: self.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, i, j):
        if self.board[i][j] is None:
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner(i, j):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw", "The game is a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, i, j):
        # Check row
        if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current_player:
            return True
        # Check column
        if self.board[0][j] == self.board[1][j] == self.board[2][j] == self.current_player:
            return True
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player):
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = None
                self.buttons[i][j].config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()