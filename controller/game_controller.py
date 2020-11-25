from controller.interface_view import IView
from helper.board_position import BoardPosition
from models.game_manager import GameManager


class GameController:

    def __init__(self, view: IView, gameManager: GameManager):
        self.view = view
        self.gameManager = gameManager

    def clickField(self, x, y):
        if self.gameManager.isPieceSelected is False:
            if self.gameManager.selectPiece(BoardPosition(x, y)):
                self.view.update()
        else:
            if self.gameManager.moveSelectedPiece(BoardPosition(x, y)):
                self.view.update()

    def getBoardState(self):
        return self.gameManager.getBoardState()
