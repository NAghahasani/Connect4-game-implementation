# 🎮 Connect4 game implementation using AI

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
