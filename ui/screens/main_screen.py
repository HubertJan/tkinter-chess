#from controller.chessController import ChessController
from controller.interface_view import IView
#from helper.board_state import BoardState
from ui.screen import Screen


class MainScreen(Screen, IView):
    ROUTENAME = "/chess"

    def __init__(self):
        print()
        #self.chessController = ChessController()

    def initBuild(self):
        print()

    def clear(self):
        print()
