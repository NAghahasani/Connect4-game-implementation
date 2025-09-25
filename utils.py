import numpy as np
from game import PLAYER, AI

def evaluate_board(board, piece):
    """
    Evaluate the board and return a score based on potential winning moves and threats.
    A positive score favors AI, negative score favors Player.
    
    Args:
        board: numpy array representing the game board
        piece: the piece being evaluated (either AI or PLAYER)
    
    Returns:
        score: numerical evaluation of the board position
    """
    score = 0
    
    # Get board dimensions
    rows, cols = board.shape
    
    # Evaluate horizontal windows
    for r in range(rows):
        for c in range(cols - 3):
            window = list(board[r, c:c+4])
            score += evaluate_window(window, piece)
    
    # Evaluate vertical windows
    for r in range(rows - 3):
        for c in range(cols):
            window = list(board[r:r+4, c])
            score += evaluate_window(window, piece)
    
    # Evaluate diagonal windows (positive slope)
    for r in range(rows - 3):
        for c in range(cols - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)
    
    # Evaluate diagonal windows (negative slope)
    for r in range(3, rows):
        for c in range(cols - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)
    
    # Give extra weight to center columns
    center_array = board[:, cols//2-1:cols//2+2]
    center_count = np.count_nonzero(center_array == piece)
    score += center_count * 3
    
    return score

def evaluate_window(window, piece):
    """
    Helper function to evaluate a window of 4 positions.
    """
    score = 0
    
    # Count pieces in window
    ai_count = window.count(AI)
    player_count = window.count(PLAYER)
    empty_count = window.count(0)
    
    # Score the window
    if ai_count == 4:
        score += 100  # AI wins
    elif ai_count == 3 and empty_count == 1:
        score += 5    # AI can win next move
    elif ai_count == 2 and empty_count == 2:
        score += 2    # AI has potential
        
    if player_count == 4:
        score -= 100  # Player wins
    elif player_count == 3 and empty_count == 1:
        score -= 5    # Block player's winning move
    elif player_count == 2 and empty_count == 2:
        score -= 2    # Block player's potential
    
    return score
