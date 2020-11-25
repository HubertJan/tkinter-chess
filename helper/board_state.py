from models.gameBoard import GameBoard
from helper.board_position import BoardPosition

class BoardState:
  def __init__(self, gameBoard, selectedPiecePos):
    self.map = []
    selectedPiece = None
    if(selectedPiecePos != None):
          selectedPiece = gameBoard.getPiece(selectedPiecePos)
    for x in range(gameBoard.boardSize[0]):
      self.map.append([])
      for y in range(gameBoard.boardSize[1]):
        pos = BoardPosition(x, y)
        piece = gameBoard.getPiece(pos)
        if(piece != None):
          content = piece.text
        else:
          content = "None"
        self.map[x].append(FieldState(content))
        if(selectedPiecePos == pos):
          self.map[x][y].isSelected = True
        elif(selectedPiece != None):
          self.map[x][y].isPossible = selectedPiece.canMove(gameBoard.pieceMap, selectedPiecePos, pos)
        
class FieldState:
  def __init__(self, pieceName):
    self.piece = pieceName
    self.isSelected = False
    self.isPossible = False
    