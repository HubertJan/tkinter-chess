from abc import ABC, abstractmethod
from enum import Enum


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

    @abstractmethod
    def allPossibleMoves(self, board, currentPos):
        pass

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
