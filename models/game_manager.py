from copy import deepcopy
from math import floor

from models.game_board import GameBoard
from models.piece import Piece
from helper.board_position import BoardPosition
from helper.board_state import BoardState


class GameManager:
    currentRound = 0
    turns = []
    _playerList = []
    _currentPlayerIndex = 0
    _board = None

    # Initialisiert auf welchen GameBoard gespielt wird.
    def __init__(self, gameBoard: GameBoard):
        self._board = gameBoard
        self._playerList = ["white", "black"]
        self._selectedPiecePos = None

    def _addTurn(self, fromPos: BoardPosition, toPos: BoardPosition):
        self.turns.append([fromPos, toPos])

    def moveSelectedPiece(self, toPos: BoardPosition):
        if self._isGameFinished():
            return False
        if self._selectedPiecePos is None:
            return False
        if toPos.Y == 6:
            print("yet")
        if self._board.movePiece(self._selectedPiecePos, toPos):
            self._addTurn(self._selectedPiecePos, toPos)
            self._endTurn()
            return True
        return False

    def _isGameFinished(self):
        return self._board.canColorMove(self.currentPlayer) is False

    def selectPiece(self, pos: BoardPosition):
        piece: Piece or None = self._board.getPiece(pos)
        if piece is None:
            return False
        if piece.color is not self.currentPlayer:
            return False
        self._selectedPiecePos = pos
        return True

    def unselectPiece(self):
        self._selectedPiecePos = None

    def _endTurn(self):
        if self._currentPlayerIndex + 1 is len(self._playerList):
            self._currentPlayerIndex = 0
        else:
            self._currentPlayerIndex += 1
        self._selectedPiecePos = None

    @property
    def currentPlayer(self):
        return self._playerList[self._currentPlayerIndex]

    @property
    def isPieceSelected(self):
        return self._selectedPiecePos is not None

    def getBoardState(self):
        return BoardState(deepcopy(self._board), self._selectedPiecePos)
    
    def getRoundNumber(self):
        return floor(len(self.turns)/len(self._playerList)) + 1
