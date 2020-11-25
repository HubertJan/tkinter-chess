class BoardPosition:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __eq__(self, other):
        if not isinstance(other, BoardPosition):
            return NotImplemented

        return self.Y == other.Y and self.X == other.X
