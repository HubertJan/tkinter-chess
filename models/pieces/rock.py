from models.piece import Piece, Direction
from helper.board_position import BoardPosition


class Rock(Piece):
    name = "rock"

    def canMove(self, pieceMap, currentPos, toPos):
        pieceAtTo = self._getPiece(pieceMap, toPos)
        if pieceAtTo is None or pieceAtTo.color != self.color:
            if toPos.X == currentPos.X:
                return not self.checkIfSomethingBetween(pieceMap, currentPos, toPos, "x")
            if toPos.Y == currentPos.Y:
                return not self.checkIfSomethingBetween(pieceMap, currentPos, toPos, "y")
        return False

    def checkIfSomethingBetween(self, pieceMap, pos1, pos2, axis):
        somethingBetween = False
        if(axis == "y"):
            p1 = pos1.X
            p2 = pos2.X
        else:
            p1 = pos1.Y
            p2 = pos2.Y

        if(p1 < p2):
            stepSize = 1
        elif(p1 > p2):
            stepSize = -1
        else:
            return False
        c = p1 + stepSize
        while c != p2:
            if(axis == "y"):
                if pieceMap[c][pos1.Y] is not None:
                    somethingBetween = True
            else:
                if pieceMap[pos1.X][c] is not None:
                    somethingBetween = True
            c += stepSize
        return somethingBetween

    def canPromote(self, pieceMap, currentPos):
        return None
