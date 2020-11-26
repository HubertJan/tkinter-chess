from tkinter import Frame, Button
from PIL import ImageTk, Image

from helper.board_state import BoardState
from controller.game_controller import GameController
from controller.interface_view import IView
from models.game_manager import GameManager
from models.game_board import GameBoard
from models.pieces.pawn import Pawn


class ChessBoard(Frame, IView):

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
                    self._changeFieldImage(x, y, self._images[state.map[x][y].piece][state.map[x][y].color][sel])

    def createClickFieldFunc(self, x, y):
        return lambda: self.clickField(x, y)

    def _changeFieldImage(self, x, y, img):
        self._board[x][y].config(image=img)

    def loadImages(self):
        self._images = {}

        self._images[Pawn.text] = {}
        self._images[Pawn.text]["black"] = [None] * 2

        img = Image.open("IMG/figure/chess-pawn.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._images[Pawn.text]["black"][0] = ImageTk.PhotoImage(img)

        img = Image.open("IMG/figure/chess-pawn-black-select.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._images[Pawn.text]["black"][1] = ImageTk.PhotoImage(img)

        self._images[Pawn.text]["white"] = [None] * 2
        img = Image.open("IMG/figure/chess-pawn-white.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._images[Pawn.text]["white"][0] = ImageTk.PhotoImage(img)

        img = Image.open("IMG/figure/chess-pawn-white-select.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._images[Pawn.text]["white"][1] = ImageTk.PhotoImage(img)

        img = Image.open("IMG/figure/chess-king.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._kingImage = ImageTk.PhotoImage(img)

        img = Image.open("IMG/figure/empty.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self._images["None"] = ImageTk.PhotoImage(img)

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
                                             image=self._images["None"],
                                             borderwidth=0,  command=self.createClickFieldFunc(i, u)))
                self._board[i][u].grid(row=u, column=i)

        self.gameController=GameController(self, GameManager(GameBoard()))
        self.updateBoard(self.gameController.getBoardState())

