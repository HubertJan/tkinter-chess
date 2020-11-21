import GameBoard from "/gameBoard"
import Piece from "/piece"

object = GameManager()


class GameManager:
  currentRound = 0
  turns = []
  _playerList = []
  _currentPlayerIndex = 0
  _board = None
  
  #Initialisiert auf welchen GameBoard gespielt wird.
  def __init__(self, gameBoard):
    self._board = gameBoard
    self._playerList = ["white", "black"]
  
  def playTurn(self, from, to):
    if(_board.pieceMap[from].color == self._currentPlayer):
      turns.append([from, to])
      self._endTurn()
  
  def _endTurn(self):
    if(self._currentPlayerIndex == self._playerList.len()):
      self._currentPlayerIndex = 0
    self._currentPlayerIndex += 1
    
  @property
    def _currentPlayer(self):
        return self._playerList[_currentPlayerIndex]