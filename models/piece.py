from abc import ABC, abstractmethod
from enum import Enum

from helper.board_position import BoardMove, BoardPosition, BoardChange

class Direction(Enum):
    UP = 1
    DOWN = 2


class Piece(ABC):
    def __init__(self, color, isKing):
        self.color = color #Playername which owns the piece
        self.isKing = isKing #If king, piece is not allowed to die

    @property
    @abstractmethod
    def name(self):
        pass

    def allMoves(self, pieceMap, currentPos) -> list[BoardMove]:
        moves = []

        for x in range(len(pieceMap)):
            for y in range(len(pieceMap[x])):
                if self.canMove(pieceMap, currentPos, BoardPosition(x, y)):
                    triggerChange = BoardChange(currentPos, BoardPosition(x, y))
                    boardMove = BoardMove(triggerChange)
                    moves.append(boardMove)
        return moves

    @abstractmethod
    def canMove(self, board, currentPos, toPos):
        #Check if move is valid, if yes return true, otherwise false
        pass

    def _getPiece(self, pieceMap, pos):
        #shortway to extract pieces from pieceMap through position
        return pieceMap[pos.X][pos.Y]

    @abstractmethod
    def canPromote(self, pieceMap, currentPos):
        pass
