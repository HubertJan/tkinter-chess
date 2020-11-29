from tkinter import Frame, Button, Label, font
from PIL import ImageTk, Image

from helper.board_state import BoardState
from models.pieces.pawn import Pawn
from models.pieces.knight import Knight
from models.pieces.rock import Rock
from models.pieces.bishop import Bishop
from models.pieces.king import King
from models.pieces.queen import Queen
from controller.game_controller import GameController
from controller import interface_view


class SelectFigureFrame(Frame):
    def _loadPieceImage(self, text, colors: list):
        self.images[text] = {}
        for color in colors:
            self.images[text][color] = [None] * 2
            for i in range(2):
                if(i == 1):
                    textIsSelect = "-select"
                else:
                    textIsSelect = ""
                img = Image.open(
                    f'IMG/figure/{text}-{color}{textIsSelect}.png')
                img = img.resize((125, 125), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.images[text][color][i] = img

    def _selectFigure(self, figure):
        self.selectedFigure = figure
        self.view.update()
    

    def loadImages(self):
        self.images = {}
        colors = ["black", "white"]

        self._loadPieceImage(Pawn.name, colors)
        self._loadPieceImage(Knight.name, colors)
        self._loadPieceImage(King.name, colors)
        self._loadPieceImage(Rock.name, colors)
        self._loadPieceImage(Bishop.name, colors)
        self._loadPieceImage(Queen.name, colors)

        img = Image.open("IMG/figure/empty.png")
        img = img.resize((125, 125), Image.ANTIALIAS)
        self.images["None"] = ImageTk.PhotoImage(img)
        img = Image.open("IMG/possible.png")
        img = img.resize((125, 125), Image.ANTIALIAS)
        self.images["Possible"] = ImageTk.PhotoImage(img)

    def __init__(self, master, view, color):
        super().__init__(master)
        self.loadImages()
        self.view = view

        self.selectedFigure = -1

        backgroundFrame = Frame(
            master=self, bg="#FFF", width=1000, height=800)
        backgroundFrame.place(x=0, y=0)

        FrameChange = Frame(master=backgroundFrame,
                            bg="#417D9E", width=840, height=300)
        FrameChange.place(anchor="center", relx=0.5, rely=0.5)

        LabelChange = Label(master=FrameChange, text="Umwandeln zu",
                            fg="#fff", bg="#417D9E")
        LabelChange["font"] = font.Font(family='Arial', size=40, weight='bold')
        LabelChange.place(anchor="center", relx=0.5, rely=0.2)

        ButtonSelectKnight = Button(
            master=FrameChange, image=self.images["knight"][color][0],  borderwidth=0, bg="#417D9E", activebackground="#417D9E",
            command=lambda:[ self._selectFigure(0)] )
        ButtonSelectKnight.place(
            anchor="center", relx=0.2, rely=0.6, width=125, height=125)

        ButtonSelectQueen = Button(
            master=FrameChange, image=self.images["bishop"][color][0],  borderwidth=0, bg="#417D9E", activebackground="#417D9E",
            command=lambda:[ self._selectFigure(1)])
        ButtonSelectQueen.place(anchor="center", relx=0.4,
                                rely=0.6, width=125, height=125)

        ButtonSelectRok = Button(
            master=FrameChange, image=self.images["rock"][color][0],  borderwidth=0, bg="#417D9E", activebackground="#417D9E",
            command= lambda: self._selectFigure(2))
        ButtonSelectRok.place(anchor="center", relx=0.6,
                              rely=0.6, width=125, height=125)

        ButtonSelectBishop = Button(
            master=FrameChange, image=self.images["queen"][color][0],  borderwidth=0, bg="#417D9E", activebackground="#417D9E",
            command=lambda : self._selectFigure(3))
        ButtonSelectBishop.place(
            anchor="center", relx=0.8, rely=0.6, width=125, height=125)
