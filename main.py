import random
import sys
import pygame
from game import ConnectFourGame, PLAYER, AI
from gui import ConnectFourGUI, RADIUS, SQUARESIZE
import engine

def main():
    gui = ConnectFourGUI()
    mode = gui.menu_loop()
    ROW_COUNT, COLUMN_COUNT = gui.get_board_size()
    game = ConnectFourGame(ROW_COUNT, COLUMN_COUNT)

    if mode == 'human':
        run_human_vs_human(game, gui)
    elif mode == 'ai':
        run_player_vs_ai(game, gui)
    elif mode == 'ai_vs_ai':
        run_ai_vs_ai(game, gui)


def run_human_vs_human(game, gui):
    turn = 0
    game_over = False
    game.reset()
    gui.draw_board(game.board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(gui.screen, (0, 0, 0), (0, 0, gui.screen.get_width(), SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(gui.screen, (255, 0, 0), (posx, SQUARESIZE // 2), RADIUS)
                else:
                    pygame.draw.circle(gui.screen, (255, 255, 0), (posx, SQUARESIZE // 2), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                col = posx // SQUARESIZE

                if game.is_valid_location(col):
                    row = game.get_next_open_row(col)

                    if turn == 0:
                        game.drop_piece(row, col, PLAYER)
                        if game.winning_move(PLAYER):
                            game.game_over = True
                            game.winner = "Player"
                        elif not game.winning_move(PLAYER) and game.is_draw():  # Check draw only if no winner
                            game.game_over = True
                            game.winner = "Draw"
                        turn = 1
                    else:
                        game.drop_piece(row, col, AI)
                        if game.winning_move(AI):
                            game.game_over = True
                            game.winner = "Player2"
                        elif not game.winning_move(AI) and game.is_draw():  # Check draw only if no winner
                            game.game_over = True
                            game.winner = "Draw"
                        turn = 0

                    gui.draw_board(game.board)

        if game.game_over:
            pygame.time.wait(1000)
            action = gui.end_page_loop(game.winner)
            if action == "restart":
                game.reset()
                gui.draw_board(game.board)
                turn = 0
                game.game_over = False
            elif action == "quit":
                pygame.quit()
                sys.exit()


def run_player_vs_ai(game, gui):
    turn = 0
    game_over = False
    game.reset()
    gui.draw_board(game.board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(gui.screen, (0, 0, 0), (0, 0, gui.screen.get_width(), SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(gui.screen, (255, 0, 0), (posx, SQUARESIZE // 2), RADIUS)
                else:
                    pygame.draw.circle(gui.screen, (255, 255, 0), (posx, SQUARESIZE // 2), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
                posx = event.pos[0]
                col = posx // SQUARESIZE

                if game.is_valid_location(col):
                    row = game.get_next_open_row(col)
                    game.drop_piece(row, col, PLAYER)

                    if game.winning_move(PLAYER):
                        game.game_over = True
                        game.winner = "Player"
                    elif not game.winning_move(PLAYER) and game.is_draw():  # Check draw only if no winner
                        game.game_over = True
                        game.winner = "Draw"

                    gui.draw_board(game.board)
                    turn = 1

        if turn == 1 and not game.game_over:
            col, _ = engine.minimax(game, depth=4, maximizing_player=True)  # Now using Minimax
            row = game.get_next_open_row(col)
            pygame.time.wait(500)  # Add a 500ms delay
            game.drop_piece(row, col, AI)

            if game.winning_move(AI):
                game.game_over = True
                game.winner = "AI"
            elif not game.winning_move(AI) and game.is_draw():  # Check draw only if no winner
                game.game_over = True
                game.winner = "Draw"

            gui.draw_board(game.board)
            turn = 0

        if game.game_over:
            pygame.time.wait(1000)
            action = gui.end_page_loop(game.winner)
            if action == "restart":
                game.reset()
                gui.draw_board(game.board)
                turn = 0
                game.game_over = False
            elif action == "quit":
                pygame.quit()
                sys.exit()


def run_ai_vs_ai(game, gui):
    turn = 0
    game_over = False
    game.reset()
    gui.draw_board(game.board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if turn == 0 and not game.game_over:
            col, _ = engine.expectimax(game, depth=4, maximizing_player=True)
            row = game.get_next_open_row(col)
            
             #col = random.choice(game.get_valid_locations())
             #row = game.get_next_open_row(col)
            pygame.time.wait(500)  # Add a 500ms delay
            game.drop_piece(row, col, PLAYER)
            pygame.time.wait(100)

            if game.winning_move(PLAYER):
                game.game_over = True
                game.winner = "Player"
            elif not game.winning_move(PLAYER) and game.is_draw():  # Check draw only if no winner
                game.game_over = True
                game.winner = "Draw"

            gui.draw_board(game.board)
            turn = 1

        if turn == 1 and not game.game_over:
            col, _ = engine.alpha_beta_pruning(game, depth=4, alpha=-float('inf'), beta=float('inf'), maximizing_player=False)
            row = game.get_next_open_row(col)
            pygame.time.wait(500)  # Add a 500ms delay
            game.drop_piece(row, col, AI)

            if game.winning_move(AI):
                game.game_over = True
                game.winner = "AI"
            elif not game.winning_move(AI) and game.is_draw():  # Check draw only if no winner
                game.game_over = True
                game.winner = "Draw"

            gui.draw_board(game.board)
            turn = 0

        if game.game_over:
            pygame.time.wait(1000)
            action = gui.end_page_loop(game.winner)
            if action == "restart":
                game.reset()
                gui.draw_board(game.board)
                turn = 0
                game.game_over = False
            elif action == "quit":
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
