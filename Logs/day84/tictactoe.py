import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Game state
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_player = "X"  # User is X
        self.user_turn = True
        self.game_over = False
        
        # Winning patterns
        self.winning_patterns = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
            [1, 5, 9], [3, 5, 7]              # diagonals
        ]
        
        # Create buttons
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text=str(i+1), font=('Arial', 24), width=5, height=2,
                              command=lambda idx=i: self.on_button_click(idx))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
    
    def on_button_click(self, index):
        if not self.user_turn or self.game_over or self.board[index] in ["X", "O"]:
            return
        
        # User move
        self.make_move(index, "X")
        
        # Check if user is about to win
        if self.check_imminent_win("X"):
            # Block the winning move
            self.block_winning_move()
        else:
            # Computer makes a random move after 2 seconds
            self.root.after(2000, self.computer_move)
    
    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index].config(text=player)
        
        if self.check_winner(player):
            self.game_over = True
            winner = "You" if player == "X" else "Computer"
            messagebox.showinfo("Game Over", f"{winner} win!")
            return
        
        if self.check_draw():
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a draw!")
            return
    
    def check_imminent_win(self, player):
        # Check if the player is one move away from winning
        for pattern in self.winning_patterns:
            count = 0
            empty_pos = None
            for pos in pattern:
                if self.board[pos-1] == player:
                    count += 1
                elif self.board[pos-1] not in ["X", "O"]:
                    empty_pos = pos-1
            if count == 2 and empty_pos is not None:
                return True
        return False
    
    def block_winning_move(self):
        # Find and block the imminent win
        for pattern in self.winning_patterns:
            x_count = 0
            empty_pos = None
            for pos in pattern:
                if self.board[pos-1] == "X":
                    x_count += 1
                elif self.board[pos-1] not in ["X", "O"]:
                    empty_pos = pos-1
            if x_count == 2 and empty_pos is not None:
                self.make_move(empty_pos, "O")
                return
    
    def computer_move(self):
        if self.game_over:
            return
        
        
        available_positions = [i for i, val in enumerate(self.board) if val not in ["X", "O"]]
        
        if available_positions:
            
            random_pos = random.choice(available_positions)
            self.make_move(random_pos, "O")
    
    def check_winner(self, player):
        for pattern in self.winning_patterns:
            if all(self.board[pos-1] == player for pos in pattern):
                return True
        return False
    
    def check_draw(self):
        return all(cell in ["X", "O"] for cell in self.board)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()