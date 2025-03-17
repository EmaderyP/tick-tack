import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=("Arial", 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)

    def button_click(self, row, col):
        button = self.master.grid_slaves(row=row, column=col)[0]
        if button["text"] == " ":
            button["text"] = self.current_player
            self.board[row * 3 + col] = self.current_player
            if self.check_win():
                tk.messagebox.showinfo("Tic Tac Toe", f"{self.current_player} wins!")
                self.reset_board()
            elif " " not in self.board:
                tk.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                if self.current_player == "X":
                    self.current_player = "O"
                    row, col = self.computer_move()
                    button = self.master.grid_slaves(row=row, column=col)[0]
                    button["text"] = self.current_player
                    self.board[row * 3 + col] = self.current_player
                    if self.check_win():
                        tk.messagebox.showinfo("Tic Tac Toe", f"{self.current_player} wins!")
                        self.reset_board()
                    elif " " not in self.board:
                        tk.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                        self.reset_board()
                    else:
                        self.current_player = "X"
                else:
                    self.current_player = "X"

    def check_win(self):
        win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_board(self):
        for button in self.master.grid_slaves():
            button["text"] = " "
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == " "]
        return divmod(random.choice(available_moves), 3)


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
