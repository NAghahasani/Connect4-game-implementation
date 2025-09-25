<<<<<<< HEAD



# Connect Four AI Project

This project is an implementation of Connect Four using Python and Pygame. The project is organized into multiple files to separate the game logic, graphical interface, AI algorithms, and utility functions. Students are encouraged to experiment with and implement various AI algorithms (Minimax, Alpha-Beta Pruning, and Expectimax) in the `engine.py` file.

## Project Structure

```
connect_four/
├── engine.py         # AI algorithms (implement your AI functions here)
├── game.py           # Game rules and board logic
├── gui.py            # Pygame graphical rendering
├── main.py           # Main game loop and execution
├── utils.py          # Helper functions for board evaluation and move generation
├── README.md         # Project instructions and guidelines
└── requirements.txt  # Dependencies (pygame, numpy)
```

## Requirements

- Python 3.x
- Pygame
- Numpy

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

## How to Run

Start the game by running:

```bash
python main.py
```

## Game Modes and Controls

- **Human vs. AI:** Click on a column in the game window to drop your piece.
- **AI vs. AI:** Modify the main loop in `main.py` to have both players controlled by the AI algorithms.
- **Restart:** Click on the "Restart" button (displayed in the upper-right corner) to reset the game.

## AI Implementation

In `engine.py`, you will find the following function stubs:

- `minimax(board, depth, maximizing_player)`
- `alpha_beta_pruning(board, depth, alpha, beta, maximizing_player)`
- `expectimax(board, depth, maximizing_player)`

These functions should be implemented to evaluate board states (using the heuristic functions provided in `utils.py`) and determine the best move. You can adjust the search depth in these functions to create different difficulty levels.

## Additional Notes

- **Board Representation:** The game board is a 6×6 numpy array defined in `game.py`.
- **Game Logic:** The game logic (e.g., placing pieces, checking for wins/draws) is encapsulated in the `ConnectFourGame` class.
- **Graphical Interface:** The `ConnectFourGUI` class in `gui.py` uses Pygame to render the game board, display pieces, highlight winning moves, and manage user inputs.
- **Utility Functions:** Functions for board evaluation and move generation are available in `utils.py` to help with AI development.

Happy coding and have fun building your AI for Connect Four!
```
=======
# 🎮 Connect4
Implementation of the Connect Four game with AI using Minimax, Alpha-Beta Pruning, and Expectimax algorithms
![Connect4 Screenshot](https://media.licdn.com/dms/image/v2/D4D12AQG6AJxOQyUtzA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1669930067210?e=2147483647&v=beta&t=tD1jGhLGeDSvSYYC5yiljfmnk6VB5tzTcA3b_p_GGxE)

A project implementing an AI for the **Connect4** game using **Minimax**, **Alpha-Beta Pruning**, and **Expectimax** algorithms.  
This project demonstrates game-tree search, utility evaluation, and intelligent decision-making strategies. 🧠💻

## ✨ Features
- 🔹 **Minimax** for optimal decisions in deterministic moves.
- 🔹 **Alpha-Beta Pruning** to speed up search by ignoring unnecessary nodes.
- 🔹 **Expectimax** for handling random elements in the game.
- 🔹 Utility function (`evaluate_board`) evaluates board positions and weights central columns.
- 🔹 AI vs AI, AI vs Random, and AI vs Human scenarios tested.

## 🛠 Tech Stack
- Python 🐍
- Standard libraries (no external dependencies)

## 📊 Results
- Minimax & Alpha-Beta perform well in AI vs AI scenarios.
- Expectimax is better against random opponents due to probabilistic evaluation.
- Depth 4 search balances accuracy and computation time for Connect4.

## 🚀 How to Run
1. Clone the repository: `git clone <repo-link>`
2. Run the main AI script: `python connect4_ai.py`

> "Choosing the best move is about balancing strategy, evaluation, and prediction." 🎯
>>>>>>> 1c086ed12ffd0abad3c6dd4c2a21bd4503a8a062
