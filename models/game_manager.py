from copy import deepcopy
from math import floor
from models.renewable_timer import RenewableTimer

from models.game_board import GameBoard
from models.piece import Piece
from helper.board_position import BoardPosition
from helper.board_state import BoardState



class GameManager:
   

    # Initialisiert auf welchen GameBoard gespielt wird.
    def __init__(self, gameBoard: GameBoard, time):
        self. currentRound = 0
        self.turns = []
        self._playerList = []
        self._currentPlayerIndex = 0
        self._board = None

        self._board = gameBoard
        self._playerList = ["white", "black"]
        self._playerNameList = ["Weiß", "Schwarz"]
        self._selectedPiecePos = None
        self._isPromoting = False
        gameOverTime = time
        self._playerTimerList = [RenewableTimer(gameOverTime),RenewableTimer(gameOverTime)]
        self._playerTimerList[self._currentPlayerIndex].start()
        self._playerTimerList[1].start()
        self._playerTimerList[1].pause()

    def _addTurn(self, fromPos: BoardPosition, toPos: BoardPosition):
        self.turns.append([fromPos, toPos])

    def moveSelectedPiece(self, toPos: BoardPosition):
        if self.isGameFinished() != False:
            return False
        if self._selectedPiecePos is None:
            return False
        if self._board.movePiece(self._selectedPiecePos, toPos):
            self._addTurn(self._selectedPiecePos, toPos)
            if self._board.canPromote(toPos):
                self._selectedPiecePos = toPos
                self._isPromoting = True
                return True
            self._endTurn()
            return True
        return False

    def isGameFinished(self):
        if self._playerTimerList[self._currentPlayerIndex].getRemainingTime() <= 0:
            return self._playerNameList[self._currentPlayerIndex] + " hat gewonnen."
        if self._board.isStalemate(self.currentPlayer):
            return "Unentschieden"
        if  self._board.canColorMove(self.currentPlayer) is False:
            return self._playerNameList[self._currentPlayerIndex] + " hat gewonnen."
        return False
        
    def selectPiece(self, pos: BoardPosition):
        piece: Piece or None = self._board.getPiece(pos)
        if piece is None:
            return False
        if piece.color is not self.currentPlayer:
            return False
        self._selectedPiecePos = pos
        return True
    
    def selectPromote(self, pieceName):
        if self._isPromoting == False:
            return
        
        self._board.promotePiece(self._selectedPiecePos, pieceName)
        self._isPromoting = False
        self._endTurn()

    def unselectPiece(self):
        self._selectedPiecePos = None

    def _endTurn(self):
        self._playerTimerList[self._currentPlayerIndex].pause()

        if self._currentPlayerIndex + 1 is len(self._playerList):
            self._currentPlayerIndex = 0
        else:
            self._currentPlayerIndex += 1
        self._selectedPiecePos = None

        self._playerTimerList[self._currentPlayerIndex].resume()

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
    
    def getIsPromoting(self):
        return self._isPromoting
    
    def getTime(self):
        print( self._playerTimerList[self._currentPlayerIndex].getRemainingTime())
        return self._playerTimerList[self._currentPlayerIndex].getRemainingTime()
