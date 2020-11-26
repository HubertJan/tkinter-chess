from tkinter import Frame, Button


class ChessBoard(Frame):

    def setBoard(self):
        print()

    def clickField(self, x, y):
        print("x:")
        print(x)
        print("y:")
        print(y)

    def createClickFieldFunc(self, x, y):
        return lambda: self.clickField(x, y)

    def __init__(self, master):
        super().__init__(master)
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
                                          activebackground=color, borderwidth=0, width=12, height=6, command=self.createClickFieldFunc(i, u)))
                self._board[i][u].grid(row=u, column=i)
