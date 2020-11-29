from tkinter import Frame, Button
from PIL import ImageTk, Image

from helper.board_state import BoardState

class ChessBoard(Frame):

    def clickField(self, x, y):
        self.gameController.clickField(x, y)

    def updateBoard(self, state: BoardState, currentPlayer):
        for x in range(len(state.map)):
            for y in range(len(state.map[x])):
                if(state.map[x][y].piece == "None"):
                    if state.map[x][y].isPossible:
                        self._changeFieldImage(x, y, self.images["Possible"])
                    else:
                        self._changeFieldImage(x, y, self.images["None"])
                else:
                    if not state.map[x][y].isPossible and state.map[x][y].color != currentPlayer:
                        self._changeButtonStatus(x,y, "disabled")
                    else:
                        self._changeButtonStatus(x,y, "normal")
                    if state.map[x][y].isSelected:
                        sel = 1
                    else:
                        sel = 0
                    self._changeFieldImage(
                        x, y, self.images[state.map[x][y].piece][state.map[x][y].color][sel])

    def createClickFieldFunc(self, x, y):
        return lambda: self.clickField(x, y)

    def _changeFieldImage(self, x, y, img):
        self._board[x][y].config(image=img)
    
    def _changeButtonStatus(self, x, y, sta="normal"):
        self._board[x][y].config(state=sta)



    def __init__(self, master, gameController, imageHandler ):
        super().__init__(master)
        self.gameController = gameController
        self.images = imageHandler.images

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
                                             image=self.images["None"],
                                             borderwidth=0,  command=self.createClickFieldFunc(i, u)))
                self._board[i][u].grid(row=u, column=i)
