# Depth first:search

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


def evaluate(board):
    """Evaluates the board and returns a score based on the current state."""
    if is_winner(board, "X"):
        return 10
    elif is_winner(board, "O"):
        return -10
    elif is_draw(board):
        return 0
    return None


def dfs(board, player):
    """Performs a DFS to determine the score of the board for the AI."""
    opponent = "O" if player == "X" else "X"
    score = evaluate(board)
    if score is not None:
        return score

    scores = []
    moves = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                score = dfs(board, opponent)
                scores.append(score)
                moves.append((row, col))
                board[row][col] = " "

    if player == "X":
        max_score_index = scores.index(max(scores))
        # Return the score for the AI's best move
        return scores[max_score_index]
    else:
        min_score_index = scores.index(min(scores))
        # Return the score for the opponent's best move
        return scores[min_score_index]


def make_move_dfs(board, player):
    """Makes a move using DFS."""
    opponent = "O" if player == "X" else "X"
    best_score = -float('inf') if player == "X" else float('inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                score = dfs(board, opponent)
                board[row][col] = " "
                if player == "X" and score > best_score:
                    best_score = score
                    best_move = (row, col)
                elif player == "O" and score < best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        row, col = best_move
        board[row][col] = player
    return best_move


def tic_tac_toe_dfs():
    """Main function to play the Tic-Tac-Toe game using DFS."""
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
            print(f"AI ({current_player}) is making a move...")
            move = make_move_dfs(board, current_player)
            if not move:
                print("No valid moves left for the AI.")
                break

        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "_main_":
    tic_tac_toe_dfs()
