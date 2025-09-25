from utils import evaluate_board
from game import PLAYER, AI

def minimax(game, depth, maximizing_player):
    """
    Minimax algorithm for Connect Four game.
    """
    valid_locations = game.get_valid_locations()

    # Check for terminal state
    is_terminal = game.winning_move(PLAYER) or game.winning_move(AI) or len(valid_locations) == 0
    
    if depth == 0 or is_terminal:
        if is_terminal:
            if game.winning_move(AI):
                return None, 1000000
            elif game.winning_move(PLAYER):
                return None, -1000000
            else:  # Draw
                return None, 0
        else:
            return None, evaluate_board(game.board, AI if maximizing_player else PLAYER)
    
    if maximizing_player:
        value = float('-inf')
        best_col = valid_locations[0]
        for col in valid_locations:
            row = game.get_next_open_row(col)
            temp_board = game.board.copy()
            game.drop_piece(row, col, AI)
            new_score = minimax(game, depth-1, False)[1]
            game.board = temp_board
            if new_score > value:
                value = new_score
                best_col = col
        return best_col, value
    
    else:  # minimizing player (player)
        value = float('inf')
        best_col = valid_locations[0]
        for col in valid_locations:
            row = game.get_next_open_row(col)
            temp_board = game.board.copy()
            game.drop_piece(row, col, PLAYER)
            new_score = minimax(game, depth-1, True)[1]
            game.board = temp_board
            if new_score < value:
                value = new_score
                best_col = col
        return best_col, value

def alpha_beta_pruning(game, depth, alpha, beta, maximizing_player):
    """
    Alpha-Beta Pruning algorithm for Connect Four game.
    """
    valid_locations = game.get_valid_locations()
    
    is_terminal = game.winning_move(PLAYER) or game.winning_move(AI) or len(valid_locations) == 0
    
    if depth == 0 or is_terminal:
        if is_terminal:
            if game.winning_move(AI):
                return None, 1000000
            elif game.winning_move(PLAYER):
                return None, -1000000
            else:
                return None, 0
        else:
            return None, evaluate_board(game.board, AI if maximizing_player else PLAYER)

    if maximizing_player:
        value = float('-inf')
        best_col = valid_locations[0]
        for col in valid_locations:
            row = game.get_next_open_row(col)
            temp_board = game.board.copy()
            game.drop_piece(row, col, AI)
            new_score = alpha_beta_pruning(game, depth-1, alpha, beta, False)[1]
            game.board = temp_board
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    
    else:  # minimizing player (player)
        value = float('inf')
        best_col = valid_locations[0]
        for col in valid_locations:
            row = game.get_next_open_row(col)
            temp_board = game.board.copy()
            game.drop_piece(row, col, PLAYER)
            new_score = alpha_beta_pruning(game, depth-1, alpha, beta, True)[1]
            game.board = temp_board
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

def expectimax(game, depth, maximizing_player):
    """
    Expectimax algorithm for Connect Four game.
    """
    valid_locations = game.get_valid_locations()
    
    is_terminal = game.winning_move(PLAYER) or game.winning_move(AI) or len(valid_locations) == 0
    
    if depth == 0 or is_terminal:
        if is_terminal:
            if game.winning_move(AI):
                return None, 1000000
            elif game.winning_move(PLAYER):
                return None, -1000000
            else:
                return None, 0
        else:
            return None, evaluate_board(game.board, AI if maximizing_player else PLAYER)

    if maximizing_player:
        value = float('-inf')
        best_col = valid_locations[0]
        for col in valid_locations:
            row = game.get_next_open_row(col)
            temp_board = game.board.copy()
            game.drop_piece(row, col, AI)
            new_score = expectimax(game, depth-1, False)[1]
            game.board = temp_board
            if new_score > value:
                value = new_score
                best_col = col
        return best_col, value
    
    else:  # chance node (player)
        value = 0
        for col in valid_locations:
            row = game.get_next_open_row(col)
            temp_board = game.board.copy()
            game.drop_piece(row, col, PLAYER)
            new_score = expectimax(game, depth-1, True)[1]
            game.board = temp_board
            value += new_score
        return valid_locations[0], value / len(valid_locations)
