from controller.interface_view import IView
from helper.board_position import BoardPosition
from models.game_manager import GameManager


class GameController:
    # dient als Interface zwischen den Model und der UI
    # jede Anfrage der UI oder des Models wird über diese Schnittstelle gegeben

    def __init__(self, view: IView, gameManager: GameManager):
        self.view = view
        self._gameManager = gameManager

    def clickField(self, x, y):
        # Gibt den Klick an den GameManager weiter,
        # Je nach Spielstand, ist es ein selectPiece Klick
        # oder ein Move Klick
        if self._gameManager.isPieceSelected is False:
            if self._gameManager.selectPiece(BoardPosition(x, y)):
                self.view.update()
        else:
            if self._gameManager.moveSelectedPiece(BoardPosition(x, y)):
                self.view.update()
            else:
                self._gameManager.unselectPiece()
                self.view.update()
    
    def pause(self):
        self._gameManager.pause()

    def resume(self):
        self._gameManager.resume()

    def promote(self, pawnName):
        self._gameManager.selectPromote(pawnName)

    def getBoardState(self):
        return self._gameManager.getBoardState()

    def getRoundNumber(self):
        return self._gameManager.getRoundNumber()

    def getCurrentPlayer(self):
        return self._gameManager.currentPlayer
    
    def getGameOver(self):
        return self._gameManager.isGameFinished()
    
    def getIsPromoting(self):
        return self._gameManager.getIsPromoting()
    
    def getTime(self):
        return self._gameManager.getTime()
