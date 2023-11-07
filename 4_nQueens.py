def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board):
    for row in board:
        print(" ".join(["Q" if x else "." for x in row]))

def solve_n_queens_util(board, row, n):
    if row == n:
        print_board(board)
        print("\n")
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            res = solve_n_queens_util(board, row + 1, n) or res

            board[row][col] = 0

    return res

def solve_n_queens(n, start_col):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][start_col] = 1

    return solve_n_queens_util(board, 1, n)


n = 8  
start_col = 0  

if start_col < 0 or start_col >= n:
    print("Invalid starting column. Please choose a column within the board size.")
else:
    solve_n_queens(n, start_col)
