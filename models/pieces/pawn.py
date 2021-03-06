from models.piece import Piece, Direction
from helper.board_position import BoardPosition


class Pawn(Piece):
    name = "pawn"

    def __init__(self, color, isKing, moveDir):
        super().__init__(color, isKing)
        self.moveDir = moveDir

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
            if currentPos.Y == 1:
                p = self._getPiece(pieceMap, BoardPosition(
                    currentPos.X, currentPos.Y + 1))
                if p == None:
                    moveDistance = 2
                else:
                    moveDistance = 1
            elif currentPos.Y == 6:
                p = self._getPiece(pieceMap, BoardPosition(
                    currentPos.X, currentPos.Y - 1))
                if p == None:
                    moveDistance = 2
                else:
                    moveDistance = 1
            else:
                moveDistance = 1

            if(x1 is x2 and
               (y1 - y2 >= 0 and y1 - y2 <= moveDistance)):
                return True
        elif pieceAtTo.color != self.color:
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

    def canPromote(self, pieceMap, currentPos):
        if(currentPos.Y == 7 and self.moveDir == Direction.UP or
           currentPos.Y == 0 and self.moveDir == Direction.DOWN):
            return True
        return False

