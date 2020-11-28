from controller.interface_view import IView
from helper.board_position import BoardPosition
from models.game_manager import GameManager


class GameController:

    def __init__(self, view: IView, gameManager: GameManager):
        self.view = view
        self._gameManager = gameManager

    def clickField(self, x, y):
        if self._gameManager.isPieceSelected is False:
            if self._gameManager.selectPiece(BoardPosition(x, y)):
                self.view.update()
        else:
            if self._gameManager.moveSelectedPiece(BoardPosition(x, y)):
                self.view.update()
            else:
                self._gameManager.unselectPiece()
                self.view.update()

    def getBoardState(self):
        return self._gameManager.getBoardState()

    def getRoundNumber(self):
        return self._gameManager.getRoundNumber()

    def getCurrentPlayer(self):
        return self._gameManager.currentPlayer
    
    def getGameOver(self):
        return self._gameManager.isGameFinished()
