from controller.chessController import ChessController
from controller.interface_view import IView
from helper.board_state import BoardState
from ui.screen import Screen

class ChessScreen(Screen, IView):
  ROUTENAME = "/chess"
  
  def __init__(self):
    self.chessController = ChessController()
  
  def initBuild(self):
    print()
  def clear(self):
    print()

  def update(self):
    state = self.chessController.getBoardState()
    for x in range(8):
      line = ""
      for y in range(8):
        line = state.map[x][y].piece + " "
      print(line)