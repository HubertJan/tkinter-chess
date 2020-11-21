class ChessController:
  
  
  def __init__(self):
    self.currentPiece = None
  
  def selectPiece(self, x, y):
    self.currentPiece = [x,y]
  