from tkinter import Frame, Button
from PIL import ImageTk, Image

from helper.board_state import BoardState
from controller.game_controller import GameController
from controller.interface_view import IView
from models.game_manager import GameManager
from models.game_board import GameBoard


class ChessBoard(Frame, IView):

    def setBoard(self):
        print()

    def clickField(self, x, y):
        self.gameController.clickField(x, y)

    def updateBoard(self, state: BoardState):
        for x in range(len(state.map)):
            for y in range(len(state.map[x])):
                if(state.map[x][y].piece == "None"):
                    self._changeFieldImage(x, y, "none")
                elif(state.map[x][y].isSelected == True):
                    self._changeFieldImage(x, y, "pawn_select")
                else:
                    self._changeFieldImage(x, y, "pawn")

    def createClickFieldFunc(self, x, y):
        return lambda: self.clickField(x, y)

    def _changeFieldImage(self, x, y, type):
        if(type == "pawn"):
            self._board[x][y].config(image=self._pawnImage)
        if(type == "pawn_select"):
            self._board[x][y].config(image=self._pawnSelectImage)
        elif(type == "king"):
            self._board[x][y].config(image=self._kingImage)
        elif(type == "none"):
            self._board[x][y].config(image=self._emptyImage)

    def loadImages(self):
        img = Image.open("IMG/figure/chess-pawn.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._pawnImage = ImageTk.PhotoImage(img)

        img = Image.open("IMG/figure/chess-pawn-black-select.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._pawnSelectImage = ImageTk.PhotoImage(img)

        img = Image.open("IMG/figure/chess-king.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._kingImage = ImageTk.PhotoImage(img)

        img = Image.open("IMG/figure/empty.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._emptyImage = ImageTk.PhotoImage(img)

    def update(self):
        self.updateBoard(self.gameController.getBoardState())

    def __init__(self, master):
        super().__init__(master)
        self.loadImages()

        boardHeight = 8
        boardWidth = 8
        self._board = []

        # 1. COLUMN

        for i in range(boardHeight):
            self._board.append([])
            for u in range(boardWidth):
                if((u % 2 and i % 2) or (not(u % 2) and not(i % 2))):
                    color = "#90D4E9"
                else:
                    color = "#417D9E"

                self._board[i].append(Button(master=self, bg=color,
                                             width=95, height=95,
                                             image=self._emptyImage,
                                             borderwidth=0,  command=self.createClickFieldFunc(i, u)))
                self._board[i][u].grid(row=u, column=i)

        self.gameController=GameController(self, GameManager(GameBoard()))
        self.updateBoard(self.gameController.getBoardState())

