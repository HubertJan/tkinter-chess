from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

from ui.screen import Screen
from controller.game_controller import GameController
from controller.interface_view import IView
from models.game_manager import GameManager
from models.game_board import GameBoard
from ui.screens.chess_board import ChessBoard
from ui.screens.status_bar import StatusBar


class ChessScreen(Screen, IView):
    ROUTENAME = "/chess"

    def initBuild(self):
        self.gameController = GameController(self, GameManager(GameBoard()))

        self.screenFrame = Frame()
        self.screenFrame.place(relx=0, rely=0, width=1000, height=800)

        self.statusBar = StatusBar(self.screenFrame)
        self.statusBar.place(relx=0, rely=0, width=200, height=800)
        self.chessBoard = ChessBoard(self.screenFrame, self.gameController)
        self.chessBoard.place(x=200, y=12, width=800, height=800)

        self.update()

    def clear(self):
        self.screenFrame.destroy()

    def update(self):
        if(self.gameController.getGameOver()):
            self._screenManager.navigate("/")
            return
        self.chessBoard.updateBoard(self.gameController.getBoardState())
        self.statusBar.setGameRound(self.gameController.getRoundNumber())
        currentPlayer = self.gameController.getCurrentPlayer()
        if(currentPlayer == "black"):
            self.statusBar.setCurrentPlayer("S", "#000", "#FFF")
        elif(currentPlayer == "white"):
            self.statusBar.setCurrentPlayer("W", "#FFF",  "#000")
