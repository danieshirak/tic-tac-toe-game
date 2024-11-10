from typing import List, Optional
import re

def print_welcome() -> None:
    """Display welcome message and board layout"""
    print("\nWelcome to Tic Tac Toe!\n")
    print("Board positions are numbered like a numeric keypad:")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\n")

def validate_input_security(user_input: str) -> bool:
    """Validate input for security concerns."""
    suspicious_patterns = [';', 'http', '<', '/', '\\', '&', '|', '$', '`', '(', ')']
    
    return (len(user_input) <= 10 and
            not any(pattern in user_input for pattern in suspicious_patterns) and
            re.match(r'^\s*\d+\s*$', user_input))

def get_player_input(player: str, available_moves: List[int]) -> int:
    """Get and validate player move."""
    while True:
        moves_str = ', '.join(str(move) for move in sorted(available_moves))
        print(f"Available positions: {moves_str}")
        
        try:
            user_input = input(f'Player {player}, enter position (1-9): ').strip()
            
            if not validate_input_security(user_input):
                print("❌ Invalid input! Please enter only numbers.")
                continue
            
            if not user_input:
                print("❌ Empty input! Please enter a number between 1-9.")
                continue
                
            position = int(user_input)
            
            if position < 1 or position > 9:
                print("❌ Please enter a number between 1 and 9.")
                continue
                
            if position not in available_moves:
                print("❌ That position is already taken!")
                continue
                
            return position
            
        except ValueError:
            print("❌ That's not a valid number! Please enter a number between 1-9.")

def check_row_win(board: List[str], position: int, player: str) -> bool:
    """Check if current move creates a winning row."""
    if position in [1, 2, 3]:  # Bottom row
        return board[1] == board[2] == board[3] == player
    if position in [4, 5, 6]:  # Middle row
        return board[4] == board[5] == board[6] == player
    if position in [7, 8, 9]:  # Top row
        return board[7] == board[8] == board[9] == player
    return False

def check_column_win(board: List[str], position: int, player: str) -> bool:
    """Check if current move creates a winning column."""
    if position in [1, 4, 7]:  # Left column
        return board[1] == board[4] == board[7] == player
    if position in [2, 5, 8]:  # Middle column
        return board[2] == board[5] == board[8] == player
    if position in [3, 6, 9]:  # Right column
        return board[3] == board[6] == board[9] == player
    return False

def check_diagonal_win(board: List[str], position: int, player: str) -> bool:
    """Check if current move creates a winning diagonal."""
    if position in [1, 5, 9]:  # Top-left to bottom-right
        return board[1] == board[5] == board[9] == player
    if position in [3, 5, 7]:  # Top-right to bottom-left
        return board[3] == board[5] == board[7] == player
    return False

class TicTacToe:
    """Tic Tac Toe game implementation."""
    
    def __init__(self):
        """Initialize empty game board."""
        self.board: List[str] = ['ignored'] + [' ' for _ in range(1,10)]
        self.current_winner: Optional[str] = None

    def display_board(self) -> None:
        """Display current game board state."""
        print('\n' * 100)  # Clear screen
        print(f' {self.board[7]} | {self.board[8]} | {self.board[9]} ')
        print('-----------')
        print(f' {self.board[4]} | {self.board[5]} | {self.board[6]} ')
        print('-----------')
        print(f' {self.board[1]} | {self.board[2]} | {self.board[3]} ')
        print('\n')

    def make_move(self, position: int, player: str) -> bool:
        """Make a move and check for win."""
        if self.board[position] == ' ':
            self.board[position] = player
            if self.check_winner(position, player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, position: int, player: str) -> bool:
        """Check if current move wins the game."""
        return (check_row_win(self.board, position, player) or
                check_column_win(self.board, position, player) or
                check_diagonal_win(self.board, position, player))

    def is_board_full(self) -> bool:
        """Check if board is full (tie game)."""
        return ' ' not in self.board[1:]

    def get_available_moves(self) -> List[int]:
        """Get list of empty positions."""
        return [i for i, mark in enumerate(self.board) if mark == ' ' and i != 0]

def play_game() -> None:
    """Main game loop."""
    print_welcome()
    game = TicTacToe()
    current_player = 'X'  # X goes first

    while True:
        game.display_board()
        print(f"Player {current_player}'s turn:")
        
        available_moves = game.get_available_moves()
        if not available_moves:
            print("It's a tie!")
            break

        position = get_player_input(current_player, available_moves)
        game.make_move(position, current_player)

        if game.current_winner:
            game.display_board()
            print(f'🎉 Player {current_player} wins!')
            break

        current_player = 'O' if current_player == 'X' else 'X'

    if input("\nPlay again? (y/n): ").lower().startswith('y'):
        play_game()

if __name__ == "__main__":
    play_game()