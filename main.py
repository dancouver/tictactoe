class TicTacToe:
    def __init__(self):
        # Initialize an empty board
        self.grid = [' ' for n in range(9)]  # 3x3 grid
        self.current_player = 'X'  # X always goes first
        self.game_over = False

    def subscript(self, n):
        """Show grid positions in subscript."""
        subscript_dict = {
            '1': '\u2081', '2': '\u2082', '3': '\u2083',
            '4': '\u2084', '5': '\u2085', '6': '\u2086',
            '7': '\u2087', '8': '\u2088', '9': '\u2089'
        }
        return subscript_dict.get(str(n), '')  # Return the subscript or empty string
    def display_grid(self):
        # Display the current state of the board with subscript numbers
        print("Current Grid:")
        for index in range(3):
            row = []
            for col in range(3):
                cell_index = index * 3 + col
                # Use subscript numbers for display
                cell_display = self.grid[cell_index] if self.grid[cell_index] != ' ' else self.subscript(
                    cell_index + 1)
                row.append(cell_display)
            print(" | ".join(row))
            if index < 2:
                print("---------")

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a win
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        return any(all(self.grid[i] == player for i in condition) for condition in win_conditions)

    def is_draw(self):
        # Check for a draw (if the board is full and no winners)
        return all(space == 'X' or space =='O' for space in self.grid)

    def validate_move(self, position):
        # Validate the player's move
        if position < 1 or position > 9:
            print("Invalid move! Please enter a number between 1 and 9.")
            return False
        if self.grid[position - 1] == 'X' or self.grid[position - 1] == 'O':
            print("Invalid move! The position is already taken.")
            return False
        return True

    def play_game(self):
        # Main game loop
        while not self.game_over:
            self.display_grid()
            move = input(f"Player {self.current_player}, enter your move (1-9): ")
            try:
                move = int(move)
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            if self.validate_move(move):
                self.grid[move - 1] = self.current_player

                # Check for a win
                if self.is_winner(self.current_player):
                    self.display_grid()
                    print(f"Player {self.current_player} wins!")
                    self.game_over = True

                # Check for a draw
                elif self.is_draw():
                    self.display_grid()
                    print("It's a draw!")
                    self.game_over = True

                # Switch players
                self.current_player = 'O' if self.current_player == 'X' else 'X'


# Main function to run the game
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    game = TicTacToe()
    game.play_game()
