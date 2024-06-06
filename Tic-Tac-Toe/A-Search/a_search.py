# Tic-Tac-Toe using A* Search Algorithm

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


def heuristic(board, player):
    """Heuristic evaluation of the board state."""
    score = 0
    for line in [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]:
        if line.count(player) == 2 and line.count(" ") == 1:
            score += 1
        if line.count(player) == 3:
            score += 10
    return score


def a_star(board, player):
    """Performs an A* search to determine the next move for the AI."""
    best_score = float('-inf')
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                score = heuristic(board, player)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move


def make_move_a_star(board, player):
    """Makes a move using the A* search algorithm."""
    move = a_star(board, player)
    if move:
        row, col = move
    else:
        row, col = next((r, c) for r in range(3)
                        for c in range(3) if board[r][c] == " ")
    return (row, col)


def tic_tac_toe_a_star():
    """Main function to play the Tic-Tac-Toe game using the A* search algorithm."""
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
            row, col = make_move_a_star(board, current_player)
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
    tic_tac_toe_a_star()
