#!/usr/bin/python3
"""
N Queens solver using backtracking
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """
    Recursive utility function to solve N Queens problem
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, n, solutions) or res
            board[i][col] = 0

    return res


def find_all_nqueens_solutions(n):
    """
    Solve the N Queens problem and return all solutions
    """
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    find_all_nqueens_solutions(sys.argv[1])
