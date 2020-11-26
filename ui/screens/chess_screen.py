from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

from ui.screen import Screen
from controller.interface_view import IView
from ui.screens.chess_board import ChessBoard
from ui.screens.status_bar import StatusBar


class ChessScreen(Screen, IView):
    ROUTENAME = "/chess"

    def initBuild(self):
        screenFrame = Frame()
        screenFrame.place(relx=0, rely=0, width=1000, height=800)

        statusBar = StatusBar(screenFrame)
        statusBar.place(relx=0, rely=0, width=200, height=800)
        chessBoard = ChessBoard(screenFrame)
        chessBoard.place(x=200, y=12, width=800, height=800)

    def clear(self):
        print()

    def update(self):
        print()
