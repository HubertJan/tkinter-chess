from tkinter import font, Canvas,  messagebox, Frame
from PIL import ImageTk, Image
import time
import threading

from ui.screen import Screen
from controller.game_controller import GameController
from controller.interface_view import IView
from models.game_manager import GameManager
from models.game_board import GameBoard
from models.chess_board import ChessBoard as ChessBoardModel
from ui.frames.chess_board import ChessBoard
from ui.frames.status_bar import StatusBar
from ui.frames.select_figure_frame import SelectFigureFrame


class ChessScreen(Screen, IView):
    ROUTENAME = "/chess"
    FIGURE_TO_TEXT = ["knight", "bishop", "rock", "queen"]

    def buttonBackClick(self):
        # Erstellt Fenster, um sicherzugehen ob Spieler wirklich Runde beenden will
        self._pause()
        response = messagebox.askquestion("Runde verlassen ", "Möchtest du die Runde wirklich verlassen?",
                                          icon='warning')
        if response == "yes":
            self.goBack()
        else:
            self._resume()

    def _pause(self):
        # Stoppt die Zeit, Spielfluß
        self.statusBar.setTime(self.gameController.getTime())
        self._isPaused = True
        self.statusBar.setPauseButton(False)
        self.gameController.pause()

    def _resume(self):
        # Restartet die Zeit und Spielfluß
        self._isPaused = False
        self.statusBar.setPauseButton(True)
        self.gameController.resume()

    def buttonClick(self):
        if self._isPaused == False:
            self._pause()
        else:
            self._resume()

    def goBack(self):
        self._screenManager.navigate("/")

    def initBuild(self, time):
        board = ChessBoardModel("black", "white")
        self._isPaused = False
        gameManager = GameManager(board, time)
        self.gameController = GameController(self, gameManager)
        self.selectMenu = None

        self.screenFrame = Frame()
        self.screenFrame.place(relx=0, rely=0, width=1000, height=800)

        self.statusBar = StatusBar(
            self.screenFrame, self.buttonClick, self.buttonBackClick)
        self.statusBar.place(relx=0, rely=0, width=200, height=800)
        self.chessBoard = ChessBoard(
            self.screenFrame, self.gameController, self._screenManager.imageHandler)
        self.chessBoard.place(x=200, y=12, width=800, height=800)

        threading.Timer(1, lambda: [
            self.update(onlyClock=True)
        ]).start()

        self.update()

    def clear(self):
        self.chessBoard.destroy()
        self.statusBar.destroy()
        self.screenFrame.destroy()
        del self.gameController
        self.gameController = None

    def timerFunc(self):
        if self.gameController != None:
            self.update(
                onlyClock=True)

    def update(self, onlyClock=False):
        # If timer is still running after game is finished
        if self.gameController == None:
            return

        if self.gameController.getIsPromoting():
            if self.selectMenu == None:
                #Erstellt Auswahlfenster für Promoting
                self.selectMenu = SelectFigureFrame( self.screenFrame, self, self.gameController.getCurrentPlayer())
                self.selectMenu.place(x=0, y=0, width=1000, height=800)
                return
            else:
                # Führt Promotion aus, löscht Promoting Fenster
                if self.selectMenu.selectedFigure != -1:
                    self.gameController.promote(self.FIGURE_TO_TEXT[self.selectMenu.selectedFigure])
                    threading.Timer(1, self.timerFunc).start()
                    self.selectMenu.destroy()
                    del self.selectMenu
                    self.selectMenu = None
                else:
                    return

        self.statusBar.setTime(self.gameController.getTime()) #Zeitzähler wird aktuellisiert
        gameOver = self.gameController.getGameOver()

        if gameOver != False:
            self._screenManager.navigate("/end", gameOver)
            return

        if onlyClock:
            #Startet process, der die Zeitzähler alle 1s aktuellisiert, neu
            threading.Timer(1, lambda: [
                self.update(onlyClock=True)
            ]).start()
            return

        self.chessBoard.updateBoard(
            self.gameController.getBoardState(), self.gameController.getCurrentPlayer())
        self.statusBar.setGameRound(self.gameController.getRoundNumber())
        currentPlayer = self.gameController.getCurrentPlayer()
        if(currentPlayer == "black"):
            self.statusBar.setCurrentPlayer("S", "#000", "#FFF")
        elif(currentPlayer == "white"):
            self.statusBar.setCurrentPlayer("W", "#FFF",  "#000")
