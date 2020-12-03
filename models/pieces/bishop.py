from models.piece import Piece, Direction
from helper.board_position import BoardPosition, BoardMove, BoardChange


class Bishop(Piece):
    name = "bishop"

    def canMove(self, pieceMap, currentPos, toPos):
        pieceAtTo = self._getPiece(pieceMap, toPos)
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

    def canPromote(self, pieceMap, currentPos):
        return None
