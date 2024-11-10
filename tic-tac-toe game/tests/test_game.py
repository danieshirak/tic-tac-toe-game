import unittest
from src.game import (
    TicTacToe, 
    check_row_win, 
    check_column_win, 
    check_diagonal_win,
    validate_input_security
)

class TestTicTacToe(unittest.TestCase):
    """Test suite for Tic Tac Toe game."""
    
    def setUp(self):
        """Create new game instance before each test."""
        self.game = TicTacToe()

    def test_initial_board(self):
        """Verify board initialization state."""
        self.assertEqual(self.game.board[0], 'ignored')
        self.assertEqual(self.game.board[1:], [' '] * 9)
        self.assertIsNone(self.game.current_winner)

    def test_row_wins(self):
        """Test all row win conditions."""
        # Bottom row win
        self.game.board = ['ignored', 'X', 'X', 'X',  # Bottom row
                                    'O', 'O', ' ',  # Middle row
                                    ' ', ' ', ' ']  # Top row
        self.assertTrue(check_row_win(self.game.board, 2, 'X'))
        
        # Middle row win
        self.game.board = ['ignored', ' ', ' ', ' ',  
                                    'O', 'O', 'O',  
                                    'X', 'X', ' ']  
        self.assertTrue(check_row_win(self.game.board, 5, 'O'))
        
        # No win
        self.game.board = ['ignored', 'X', 'X', 'O',  
                                    ' ', ' ', ' ',  
                                    ' ', ' ', ' ']  
        self.assertFalse(check_row_win(self.game.board, 1, 'X'))

    def test_column_wins(self):
        """Test all column win conditions."""
        # Left column win
        self.game.board = ['ignored', 'X', 'O', ' ',  
                                    'X', ' ', ' ',  
                                    'X', ' ', ' ']
        self.assertTrue(check_column_win(self.game.board, 4, 'X'))
        
        # Middle column win
        self.game.board = ['ignored', ' ', 'O', ' ',  
                                    ' ', 'O', ' ',  
                                    ' ', 'O', ' ']
        self.assertTrue(check_column_win(self.game.board, 5, 'O'))

    def test_diagonal_wins(self):
        """Test all diagonal win conditions."""
        # Diagonal win
        self.game.board = ['ignored', 'X', ' ', ' ',  
                                    ' ', 'X', ' ',  
                                    ' ', ' ', 'X']
        self.assertTrue(check_diagonal_win(self.game.board, 5, 'X'))

    def test_full_game(self):
        """Test complete game scenarios."""
        # X wins
        moves = [(1, 'X'), (4, 'O'), (2, 'X'), (5, 'O'), (3, 'X')]
        for pos, player in moves:
            self.game.make_move(pos, player)
        self.assertEqual(self.game.current_winner, 'X')

    def test_tie_game(self):
        """Test tie game scenario."""
        moves = [
            (1, 'X'), (2, 'O'), (3, 'X'),
            (5, 'O'), (4, 'X'), (6, 'O'),
            (8, 'X'), (7, 'O'), (9, 'X')
        ]
        for pos, player in moves:
            self.game.make_move(pos, player)
        
        self.assertTrue(self.game.is_board_full())
        self.assertIsNone(self.game.current_winner)

    def test_invalid_moves(self):
        """Test handling of invalid moves."""
        self.game.make_move(5, 'X')
        self.assertFalse(self.game.make_move(5, 'O'))
        self.assertEqual(self.game.board[5], 'X')

    def test_input_security(self):
        """Test input security validation."""
        # Valid inputs
        self.assertTrue(validate_input_security("5"))
        self.assertTrue(validate_input_security(" 7 "))
        
        # Invalid inputs
        self.assertFalse(validate_input_security("rm -rf /"))
        self.assertFalse(validate_input_security("<script>"))
        self.assertFalse(validate_input_security("12345678910"))
        self.assertFalse(validate_input_security("abc"))

if __name__ == '__main__':
    unittest.main()