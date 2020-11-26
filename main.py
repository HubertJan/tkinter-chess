from models.game_manager import GameManager
from models.game_board import GameBoard
from controller.game_controller import GameController
from controller.interface_view import IView
from ui.screen_manager import ScreenManager

#from helper.board_position import BoardPosition
#from helper.board_state import BoardState



class ViewDisplay(IView):
    def __init__(self):
        self.gameController = GameController(self, GameManager(GameBoard()))

    def update(self):
        print("")
        state = self.gameController.getBoardState()
        for x in range(len(state.map)):
            line = ""
            for y in range(len(state.map[x])):
                if state.map[x][y].isSelected is True:
                    line += "x"
                line += state.map[x][y].piece + " "
            print(line)

    def click(self):
        self.gameController.clickField(0, 0)
        self.gameController.clickField(0, 1)
        self.gameController.clickField(0, 7)
        self.gameController.clickField(0, 6)
        self.gameController.clickField(0, 1)
        self.gameController.clickField(0, 3)
        self.gameController.clickField(0, 6)
        self.gameController.clickField(0, 4)
        self.gameController.clickField(0, 3)
        self.gameController.clickField(0, 4)

#viewDisplay = ViewDisplay()
# viewDisplay.click()

manager = ScreenManager()
manager.start()

