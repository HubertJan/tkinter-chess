class BoardPosition:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __eq__(self, other):
        # Macht das Vergleichen von zwei BoardPosition möglich
        # e.g. BoardPosition(4,4) == BoardPosition(4,4) -> True
        if not isinstance(other, BoardPosition):
            return NotImplemented

        return self.Y == other.Y and self.X == other.X


class BoardChange:
    def __init__(self, fromPos: BoardPosition, toPos: BoardPosition):
        self.fromPos = fromPos
        self.toPos = toPos

    def __eq__(self, other):
        # Macht das Vergleichen von zwei BoardPosition möglich
        # e.g. BoardPosition(4,4) == BoardPosition(4,4) -> True
        if not isinstance(other, BoardPosition):
            return NotImplemented

        return self.fromPos == other.fromPos and self.toPos == other.toPos
    
class BoardMove:
    def __init__(self, triggerChange: BoardChange, *otherChanges):
        self.triggerChange = triggerChange
        self.otherChanges = otherChanges
    
    def __eq__(self, other):
        # Macht das Vergleichen von zwei BoardPosition möglich
        # e.g. BoardPosition(4,4) == BoardPosition(4,4) -> True
        if not isinstance(other, BoardPosition):
            return NotImplemented

        return self.triggerChange == other.triggerChange and self.otherChanges == other.otherChanges
