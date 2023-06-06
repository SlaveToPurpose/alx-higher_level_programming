#!/usr/bin/python3
"""n queens problem solver"""
import sys


class NQueensSolver:
    """Solving N Queens Problem"""

    def __init__(self, n):
        """initialise variables"""
        self.n = n
        self.board = [[0 for i in range(n)] for i in range(n)]
        self.solutions = []

    def can_place_queen(self, row, col):
        """checks if a queen can be placed at the given position"""
        for i in range(row):
            if self.board[i][col] == 1:
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve_n_queens(self, row):
        """Recursive function"""
        if row == self.n:
            solution = []
            for i in range(self.n):
                queen_col = self.board[i].index(1)
                solution.append([i, queen_col])
            self.solutions.append(solution)
        else:
            for col in range(self.n):
                if self.can_place_queen(row, col):
                    self.board[row][col] = 1
                    self.solve_n_queens(row + 1)
                    self.board[row][col] = 0

    def print_solutions(self):
        """print soltions"""
        for solution in self.solutions:
            solution_str = ""
            for row, col in solution:
                solution_str += "[{}, {}], ".format(row, col)
            solution_str = solution_str[:-2]
            print(solution_str)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
N = sys.argv[1]
try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
solver = NQueensSolver(N)
solver.solve_n_queens(0)
solver.print_solutions()
