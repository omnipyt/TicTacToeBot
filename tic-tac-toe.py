import random

#Author: Ryan Horner - Tic Tac Toe Vs Computer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("--+---+--")

    def available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def minimax(self, depth, maximizing_player):
        if self.check_winner('X'):
            return -1
        if self.check_winner('O'):
            return 1
        if not self.available_moves():
            return 0

        if maximizing_player:
            max_eval = -float('inf')
            for move in self.available_moves():
                self.make_move(move, 'O')
                eval = self.minimax(depth + 1, False)
                self.board[move] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.make_move(move, 'X')
                eval = self.minimax(depth + 1, True)
                self.board[move] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.available_moves():
            self.make_move(move, 'O')
            score = self.minimax(0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def play(self):
        self.display_board()
        while True:
            human_move = int(input("Enter your move (0-8): "))
            if self.make_move(human_move, 'X'):
                self.display_board()
                if self.check_winner('X'):
                    print("You win!")
                    break
                elif not self.available_moves():
                    print("It's a draw!")
                    break

                computer_move = self.best_move()
                self.make_move(computer_move, 'O')
                self.display_board()
                if self.check_winner('O'):
                    print("Computer wins!")
                    break
                elif not self.available_moves():
                    print("It's a draw!")
                    break

if __name__ == "__main__":
    print ("Welcome to Tic Tac Toe!")
    print("Here's how the board is numbered:")
    print("\n")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8")
    print("\n")
    game = TicTacToe()
    game.play()

