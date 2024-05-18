import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = {
            'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''
        }
        self.buttons = {}
        self.create_buttons()
        self.status_label = tk.Label(root, text="Player X's turn", font=('Helvetica', 14))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def create_buttons(self):
        positions = [
            ('top-L', 0, 0), ('top-M', 0, 1), ('top-R', 0, 2),
            ('mid-L', 1, 0), ('mid-M', 1, 1), ('mid-R', 1, 2),
            ('low-L', 2, 0), ('low-M', 2, 1), ('low-R', 2, 2)
        ]
        for pos, row, col in positions:
            button = tk.Button(self.root, text='', font=('Helvetica', 20), height=3, width=6,
                               command=lambda p=pos: self.on_button_click(p))
            button.grid(row=row, column=col)
            self.buttons[pos] = button

    def on_button_click(self, position):
        if self.board[position] == '':
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif '' not in self.board.values():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.config(text=f"Player {self.current_player}'s turn")
        else:
            messagebox.showwarning("Invalid Move", "This position is already taken!")

    def check_winner(self):
        winning_combinations = [
            ['top-L', 'top-M', 'top-R'],
            ['mid-L', 'mid-M', 'mid-R'],
            ['low-L', 'low-M', 'low-R'],
            ['top-L', 'mid-L', 'low-L'],
            ['top-M', 'mid-M', 'low-M'],
            ['top-R', 'mid-R', 'low-R'],
            ['top-L', 'mid-M', 'low-R'],
            ['top-R', 'mid-M', 'low-L']
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

    def reset_game(self):
        self.board = {
            'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''
        }
        for button in self.buttons.values():
            button.config(text='')
        self.current_player = 'X'
        self.status_label.config(text="Player X's turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

