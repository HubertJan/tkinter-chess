from models.gameBoard import GameBoard
from models.piece import Piece
from helper.board_position import BoardPosition
from copy import deepcopy
from helper.board_state import BoardState

class GameManager:
  currentRound = 0
  turns = []
  _playerList = []
  _currentPlayerIndex = 0
  _board = None
  
  #Initialisiert auf welchen GameBoard gespielt wird.
  def __init__(self, gameBoard):
    self._board = gameBoard
    self._playerList = ["white","black"]
    self._selectedPiecePos = None
  
  def _addTurn(self, fromPos, toPos):
    self.turns.append([fromPos, toPos])
    
  def moveSelectedPiece(self, toPos):
    if(self._isGameFinished()):
      return False
    if(self._selectedPiecePos == None):
      return False
    if(toPos.Y == 6):
      print("yet")
    if(self._board.movePiece(self._selectedPiecePos, toPos)):
      self._addTurn(self._selectedPiecePos, toPos)
      self._endTurn()
      return True
    return False
    
  def _isGameFinished(self):
    return self._board.canColorMove(self.currentPlayer) == False
    
  def selectPiece(self, pos):
    piece = self._board.getPiece(pos)
    if(piece == None):
      return False
    if(piece.color != self.currentPlayer):
      return False
    self._selectedPiecePos = pos
    return True
    
  def _endTurn(self):
    if(self._currentPlayerIndex +1 == len(self._playerList)):
      self._currentPlayerIndex = 0
    else:
      self._currentPlayerIndex += 1
    self._selectedPiecePos = None
    
  @property
  def currentPlayer(self):
      return self._playerList[self._currentPlayerIndex]
  
  @property
  def isPieceSelected(self):
    return self._selectedPiecePos != None
  
  def getBoardState(self):
    return BoardState(deepcopy(self._board), self._selectedPiecePos)