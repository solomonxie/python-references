"""
OOD: Tic-Tac-Toe.
An n x n board, two players alternating turns, win detection along rows,
columns, and both diagonals.
"""


class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[None] * size for _ in range(size)]

    def place(self, row, col, mark):
        if self.grid[row][col] is not None:
            raise ValueError(f"Cell ({row}, {col}) already taken")
        self.grid[row][col] = mark

    def winner(self):
        lines = list(self.grid) + list(zip(*self.grid))
        lines.append([self.grid[i][i] for i in range(self.size)])
        lines.append([self.grid[i][self.size - 1 - i] for i in range(self.size)])
        for line in lines:
            if line[0] is not None and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_full(self):
        return all(cell is not None for row in self.grid for cell in row)


class Game:
    def __init__(self, players, size=3):
        self.board = Board(size)
        self.players = players
        self.turn = 0

    def play(self, row, col):
        mark = self.players[self.turn % len(self.players)]
        self.board.place(row, col, mark)
        self.turn += 1
        winner = self.board.winner()
        if winner:
            return f"{winner} wins!"
        if self.board.is_full():
            return "Draw!"
        return None


if __name__ == "__main__":
    game = Game(players=["X", "O"])
    moves = [(0, 0), (1, 1), (0, 1), (2, 2), (0, 2)]
    for row, col in moves:
        result = game.play(row, col)
        if result:
            print(result)
            break
