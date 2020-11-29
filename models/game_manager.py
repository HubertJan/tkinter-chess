from copy import deepcopy
from math import floor
from models.renewable_timer import RenewableTimer

from models.game_board import GameBoard
from models.piece import Piece
from helper.board_position import BoardPosition
from helper.board_state import BoardState
from database import Database

class GameManager:
    # Initialisiert auf welchen GameBoard gespielt wird.
    def __init__(self, gameBoard: GameBoard, time):
        self.database = Database("/records.csv")
        self. currentRound = 0
        self.turns = []
        self._playerList = []
        self._currentPlayerIndex = 0
        self._board = None
        self._isPaused = False

        self._board = gameBoard
        self._playerList = ["white", "black"]
        self._otherPlayerList = ["Schwarz", "Weiß"]
        self._selectedPiecePos = None
        self._isPromoting = False
        self.gameOverTime = time
        self._playerTimerList = [RenewableTimer(time), RenewableTimer(time)]
        self._playerTimerList[self._currentPlayerIndex].start()
        self._playerTimerList[1].start()
        self._playerTimerList[1].pause()

    def _addTurn(self, fromPos: BoardPosition, toPos: BoardPosition):
        self.turns.append([fromPos, toPos])

    def moveSelectedPiece(self, toPos: BoardPosition):
        if self._isPaused == True:
            return False

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

    def addGameToDatabase(self, winner):
        self.database.addRecord(0, self.gameOverTime, len(self.turns) + 1, winner)

    def isGameFinished(self):
        if self._isPaused == True:
            return False

        if self._playerTimerList[self._currentPlayerIndex].getRemainingTime() <= 0:
            self.addGameToDatabase(self._otherPlayerList[self._currentPlayerIndex])
            return self._otherPlayerList[self._currentPlayerIndex] + " hat gewonnen."
        if self._board.isStalemate(self.currentPlayer):
            self.addGameToDatabase("draw")
            return "Unentschieden"
        if self._board.canColorMove(self.currentPlayer) is False:
            self.addGameToDatabase(
                self._otherPlayerList[self._currentPlayerIndex])
            return self._otherPlayerList[self._currentPlayerIndex] + " hat gewonnen."
        return False

    def selectPiece(self, pos: BoardPosition):
        if self._isPaused == True:
            return False

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

    def pause(self):
        self._isPaused = True
        self._playerTimerList[self._currentPlayerIndex].pause()

    def resume(self):
        self._isPaused = False
        self._playerTimerList[self._currentPlayerIndex].resume()

    @ property
    def currentPlayer(self):
        return self._playerList[self._currentPlayerIndex]

    @ property
    def isPieceSelected(self):
        return self._selectedPiecePos is not None

    def getBoardState(self):
        return BoardState(deepcopy(self._board), self._selectedPiecePos)

    def getRoundNumber(self):
        return floor(len(self.turns)/len(self._playerList)) + 1

    def getIsPromoting(self):
        return self._isPromoting

    def getTime(self):
        print(
            self._playerTimerList[self._currentPlayerIndex].getRemainingTime())
        return self._playerTimerList[self._currentPlayerIndex].getRemainingTime()
