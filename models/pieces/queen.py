from models.piece import Piece, Direction
from helper.board_position import BoardPosition


class Queen(Piece):
    name = "queen"

    def canMove(self, pieceMap, currentPos, toPos):
        pieceAtTo = self._getPiece(pieceMap, toPos)
        if pieceAtTo is None or pieceAtTo.color != self.color:
            if toPos.X == currentPos.X:
                return not self.checkIfSomethingBetween(pieceMap, currentPos, toPos, "x")
            if toPos.Y == currentPos.Y:
                return not self.checkIfSomethingBetween(pieceMap, currentPos, toPos, "y")
        
        if pieceAtTo is None or pieceAtTo.color != self.color:
            if abs(currentPos.X - toPos.X) == abs(currentPos.Y - toPos.Y):
                if not self.checkIfSomethingBetweenVertical(pieceMap, currentPos, toPos):
                    return True
        return False

    
    def checkIfSomethingBetweenVertical(self, pieceMap, pos1, pos2):
        somethingBetween = False

        if pos1.Y < pos2.Y:
            yStep = 1
        else:
            yStep = -1
        if pos1.X < pos2.X:
            xStep = 1
        else:
            xStep = -1

        pos = pos1
        pos = BoardPosition(pos.X + xStep, pos.Y + yStep)
        while somethingBetween == False and pos != pos2:
            piece = self._getPiece(pieceMap, pos)
            if piece is not None:
                somethingBetween = True
            pos = BoardPosition(pos.X + xStep, pos.Y + yStep)
        return somethingBetween


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

    def allPossibleMoves(self, pieceMap, currentPos):
        possibleMovePos = []
        for x in range(len(pieceMap)):
            for y in range(len(pieceMap[x])):
                if self.canMove(pieceMap, currentPos, BoardPosition(x, y)):
                    possibleMovePos.append(BoardPosition(x, y))
        return possibleMovePos

    def canPromote(self, pieceMap, currentPos):
        return None
