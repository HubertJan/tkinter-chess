from models.piece import Piece, Direction
from helper.board_position import BoardPosition


class Bishop(Piece):
    name = "bishop"

    def canMove(self, pieceMap, currentPos, toPos):
        pieceAtTo = self._getPiece(pieceMap, toPos)
        if pieceAtTo is None or pieceAtTo.color != self.color:
            if abs(currentPos.X - toPos.X) == abs(currentPos.Y - toPos.Y):
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
