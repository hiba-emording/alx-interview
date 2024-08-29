#!/usr/bin/python3

"""
Defines NQueens Solver
"""

import sys


class NQueens:
    """A class: NQueens"""
    def __init__(self, N):
        """A function to create a new board"""
        self.N = N
        self.board = [[' ' for i in range(N)] for i in range(N)]
        self.result = []

    def safe(self, row, col):
        """A function to check for safe spots"""
        """ X and Y axis """
        for i in range(self.N):
            if self.board[row][i] == "Q" or self.board[i][col] == "Q":
                return False

        """ Top-Left and Down-Right"""
        r, c = row, col
        while r >= 0 and c >= 0:
            if self.board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        """ Down-Left and Top-Right """
        r, c = row, col
        while r < self.N and c < self.N:
            if self.board[r][c] == "Q":
                return False
            r += 1
            c += 1

        """ Top-Right and Down-Left """
        r, c = row, col
        while r >= 0 and c < self.N:
            if self.board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        """ Down Right and Top Left """
        r, c = row, col
        while r < self.N and c >= 0:
            if self.board[r][c] == "Q":
                return False
            r += 1
            c -= 1

        return True

    def placeQueens(self, row, queens):
        """ A function to place Queens using backtracking"""
        if row == self.N:
            self.result.append(self.positions().copy())
            return

        for i in range(self.N):
            if self.safe(row, i):
                self.board[row][i] = "Q"
                self.placeQueens(row + 1, queens)
                self.board[row][i] = " "

    def NQ_solve(self):
        """A function to check for all NQueens possible solutions"""
        self.placeQueens(0, 0)
        return self.result

    def positions(self):
        """A function to retrive placed queens"""
        solution = []
        for row in range(self.N):
            for col in range(self.N):
                if self.board[row][col] == "Q":
                    solution.append([row, col])
                    break
        return solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    N = int(sys.argv[1])
    solver = NQueens(N)
    result = solver.NQ_solve()

    for solution in result:
        print(solution)
