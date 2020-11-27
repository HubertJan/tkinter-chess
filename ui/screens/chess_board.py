from tkinter import Frame, Button
from PIL import ImageTk, Image

from helper.board_state import BoardState
from models.pieces.pawn import Pawn
from models.pieces.knight import Knight
from controller.game_controller import GameController


class ChessBoard(Frame):

    def setBoard(self):
        print()

    def clickField(self, x, y):
        self.gameController.clickField(x, y)

    def updateBoard(self, state: BoardState):
        for x in range(len(state.map)):
            for y in range(len(state.map[x])):
                if(state.map[x][y].piece == "None"):
                    self._changeFieldImage(x, y, self._images["None"])
                else:
                    if state.map[x][y].isSelected:
                        sel = 1
                    else:
                        sel = 0
                    print(state.map[x][y].piece)
                    self._changeFieldImage(
                        x, y, self._images[state.map[x][y].piece][state.map[x][y].color][sel])

    def createClickFieldFunc(self, x, y):
        return lambda: self.clickField(x, y)

    def _changeFieldImage(self, x, y, img):
        self._board[x][y].config(image=img)

    def _loadPieceImage(self, text, colors: list):
        self._images[text] = {}
        for color in colors:
            self._images[text][color] = [None] * 2
            for i in range(2):
                if(i == 1):
                    textIsSelect = "-select"
                else:
                    textIsSelect = ""
                img = Image.open(f'IMG/figure/{text}-{color}{textIsSelect}.png')
                img = img.resize((80, 80), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self._images[text][color][i] = img

    def loadImages(self):
        self._images = {}
        colors = ["black", "white"]

        self._loadPieceImage(Pawn.name, colors)
        self._loadPieceImage(Knight.name, colors)

        img = Image.open("IMG/figure/empty.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._images["None"] = ImageTk.PhotoImage(img)

    def __init__(self, master, gameController):
        super().__init__(master)
        self.gameController = gameController
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
                                             image=self._images["None"],
                                             borderwidth=0,  command=self.createClickFieldFunc(i, u)))
                self._board[i][u].grid(row=u, column=i)
