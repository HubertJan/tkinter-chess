class BoardPosition:
    #Bei
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __eq__(self, other):
        #Macht das Vergleichen von zwei BoardPosition möglich
        #e.g. BoardPosition(4,4) == BoardPosition(4,4) -> True
        if not isinstance(other, BoardPosition):
            return NotImplemented

        return self.Y == other.Y and self.X == other.X
