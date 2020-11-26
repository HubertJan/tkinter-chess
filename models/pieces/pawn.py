from models.piece import Piece, Direction
from helper.board_position import BoardPosition


class Pawn(Piece):
    text = "Pa"

    def canMove(self, pieceMap, currentPos, toPos):
        pieceAtTo = self._getPiece(pieceMap, toPos)
        if pieceAtTo is None:
            if self.moveDir == Direction.UP:
                x1 = toPos.X
                x2 = currentPos.X
                y1 = toPos.Y
                y2 = currentPos.Y
            else:
                x1 = toPos.X
                x2 = currentPos.X
                y1 = currentPos.Y
                y2 = toPos.Y
            if(x1 is x2 and
               (y1 - y2 >= 0 and y1 - y2 <= 2)):
                return True
        else:
            if self.moveDir == Direction.UP:
                x1 = toPos.X
                x2 = currentPos.X
                y1 = toPos.Y
                y2 = currentPos.Y
            else:
                x1 = toPos.X
                x2 = currentPos.X
                y1 = currentPos.Y
                y2 = toPos.Y
            if(abs(x1-x2) == 1 and
               (y1 - y2 == 1)):
                return True
        return False

    def allPossibleMoves(self, pieceMap, currentPos):
        possibleMovePos = []
        for x in range(len(pieceMap)):
            for y in range(len(pieceMap[x])):
                if self.canMove(pieceMap, currentPos, BoardPosition(x, y)):
                    possibleMovePos.append(BoardPosition(x, y))
        return possibleMovePos

    def canPromote(self, pieceMap, currentPos):
        return None
