from models.piece import Piece, Direction
from helper.board_position import BoardPosition


class Knight(Piece):
    name = "knight"

    def canMove(self, pieceMap, currentPos, toPos):
        pieceAtTo = self._getPiece(pieceMap, toPos)
        if pieceAtTo is None or pieceAtTo.color != self.color:
            if (abs(toPos.X - currentPos.X) == 2 and abs(toPos.Y - currentPos.Y) == 1) or (abs(toPos.X - currentPos.X) == 1 and abs(toPos.Y - currentPos.Y) == 2):
                return True
        return False

    def canPromote(self, pieceMap, currentPos):
        return None
