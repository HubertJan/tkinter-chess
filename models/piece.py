from abc import ABC, abstractmethod
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2


class Piece(ABC):
    def __init__(self, color, isKing, moveDir):
        self.color = color
        self.isKing = isKing
        self.moveDir = moveDir

    @property
    @abstractmethod
    def text(self):
        pass

    @abstractmethod
    def allPossibleMoves(self, board, currentPos):
        pass

    @abstractmethod
    def canMove(self, board, currentPos, toPos):
        pass

    def _getPiece(self, pieceMap, pos):
        return pieceMap[pos.X][pos.Y]

    @abstractmethod
    def canPromote(self):
        pass
