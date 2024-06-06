# Tic-Tac-Toe using Breadth First Search (BFS)

from collections import deque

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    """Checks if the specified player has won the game."""
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)

def bfs(board, player):
    """Performs a BFS to determine the next move for the AI."""
    queue = deque([(board, player)])
    while queue:
        current_board, current_player = queue.popleft()
        for row in range(3):
            for col in range(3):
                if current_board[row][col] == " ":
                    new_board = [list(r) for r in current_board]
                    new_board[row][col] = current_player
                    if is_winner(new_board, current_player):
                        return (row, col)
                    if is_draw(new_board):
                        continue
                    opponent = "O" if current_player == "X" else "X"
                    queue.append((new_board, opponent))
    return None

def make_move_bfs(board, player):
    """Makes a move using BFS."""
    move = bfs(board, player)
    if move:
        row, col = move
    else:
        row, col = next((r, c) for r in range(3) for c in range(3) if board[r][c] == " ")
    return (row, col)

def tic_tac_toe_bfs():
    """Main function to play the Tic-Tac-Toe game using BFS."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            print(f"Player {current_player}'s turn")
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = current_player
            else:
                print("Invalid move! Try again.")
                continue
        else:
            row, col = make_move_bfs(board, current_player)
            board[row][col] = current_player

        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe_bfs()
