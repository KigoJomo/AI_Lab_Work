# Tic-Tac-Toe using Depth First Search (DFS)

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

def dfs(board, player):
    """Performs a DFS to determine the next move for the AI."""
    opponent = "O" if player == "X" else "X"
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                if is_winner(board, player):
                    board[row][col] = " "
                    return (row, col)
                if not any(board[r][c] == " " for r in range(3) for c in range(3)):
                    board[row][col] = " "
                    return None
                move = dfs(board, opponent)
                board[row][col] = " "
                if move is None:
                    best_move = (row, col)
    return best_move

def make_move_dfs(board, player):
    """Makes a move using DFS."""
    move = dfs(board, player)
    if move:
        return move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return (row, col)
    return None

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
            move = make_move_dfs(board, current_player)
            if move:
                row, col = move
            else:
                row, col = next((r, c) for r in range(3) for c in range(3) if board[r][c] == " ")
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
    tic_tac_toe_dfs()
    
    
# uses a stack to explore every possible move in-depth and choses a winning move once it is found
# may be inefficient as it takes a lot of time for comeplex scenarios