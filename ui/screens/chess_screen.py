from tkinter import *
from tkinter import font, Canvas
from PIL import ImageTk, Image
import time
import threading

from ui.screen import Screen
from controller.game_controller import GameController
from controller.interface_view import IView
from models.game_manager import GameManager
from models.game_board import GameBoard
from ui.screens.chess_board import ChessBoard
from ui.screens.status_bar import StatusBar
from ui.screens.select_figure_frame import SelectFigureFrame


class ChessScreen(Screen, IView):
    ROUTENAME = "/chess"

    def create_rectangle(self, x1, y1, x2, y2, root, canvas, **kwargs):
        images = []
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = root.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            images.append(ImageTk.PhotoImage(image))
            canvas.create_image(x1, y1, image=images[-1], anchor='nw')
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

    def buttonClick(self):
        self._screenManager.navigate("/")

    def initBuild(self, time):
        board = GameBoard()
        gameManager = GameManager(board, time)
        self.gameController = GameController(self, gameManager)
        self.selectMenu = None

        self.screenFrame = Frame()
        self.screenFrame.place(relx=0, rely=0, width=1000, height=800)

        self.statusBar = StatusBar(self.screenFrame, self.buttonClick)
        self.statusBar.place(relx=0, rely=0, width=200, height=800)
        self.chessBoard = ChessBoard(self.screenFrame, self.gameController)
        self.chessBoard.place(x=200, y=12, width=800, height=800)

        threading.Timer(1, lambda: [
            self.update(onlyClock=True)
        ]).start()

        self.update()

    def clear(self):
        self.screenFrame.destroy()
        del self.gameController
        self.gameController = None
        self.chessBoard.destroy()
        self.statusBar.destroy()

    def update(self, onlyClock=False):
        #If timer is still running after game is finished
        if self.gameController == None:
            return
            
        if self.gameController.getIsPromoting():
            if self.selectMenu == None:
                self.selectMenu = SelectFigureFrame(self.screenFrame, self)
                self.selectMenu.place(x=0, y=0, width=1000, height=800)
                return
            else:
                if self.selectMenu.selectedFigure != -1:
                    self.gameController.promote("queen")
                    threading.Timer(1, lambda: [
                        self.update(onlyClock=True)
                    ]).start()
                    self.selectMenu.destroy()
                else:
                    return

        self.statusBar.setTime(self.gameController.getTime())
        if self.gameController.getGameOver():
            self._screenManager.navigate("/")
            return
        if onlyClock:
            threading.Timer(1, lambda: [
                self.update(onlyClock=True)
            ]).start()
            return

        if self.gameController.getGameOver():
            self._screenManager.navigate("/")
            return

        self.chessBoard.updateBoard(
            self.gameController.getBoardState(), self.gameController.getCurrentPlayer())
        self.statusBar.setGameRound(self.gameController.getRoundNumber())
        currentPlayer = self.gameController.getCurrentPlayer()
        if(currentPlayer == "black"):
            self.statusBar.setCurrentPlayer("S", "#000", "#FFF")
        elif(currentPlayer == "white"):
            self.statusBar.setCurrentPlayer("W", "#FFF",  "#000")
