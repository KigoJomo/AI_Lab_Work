# Tic-Tac-Toe using Min-Max Algorithm

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 10)


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


def min_max(board, depth, is_maximizing):
    """Min-Max algorithm implementation."""
    if is_winner(board, "X"):
        return 10 - depth
    if is_winner(board, "O"):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = min_max(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = min_max(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score


def make_move_min_max(board):
    """Finds the best move using the Min-Max algorithm."""
    best_score = float('-inf')
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                score = min_max(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move


def tic_tac_toe_min_max():
    """Main function to play the Tic-Tac-Toe game using the Min-Max algorithm."""
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
            row, col = make_move_min_max(board)
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
    tic_tac_toe_min_max()
