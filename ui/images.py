from PIL import ImageTk, Image

from models.pieces.pawn import Pawn
from models.pieces.knight import Knight
from models.pieces.rock import Rock
from models.pieces.bishop import Bishop
from models.pieces.king import King
from models.pieces.queen import Queen

class ImageHandler:
    # Dient zum Laden aller Bilder
    # Bilder können von hier aus aufgerufen werden
    def __init__(self):
        self._loadImages()

    def _loadPieceImage(self, text, colors: list):
        self.images[text] = {}
        for color in colors:
            self.images[text][color] = [None] * 2
            for i in range(2):
                if i == 1:
                    textIsSelect = "-select"
                else:
                    textIsSelect = ""
                img = Image.open(
                    f'IMG/figure/{text}-{color}{textIsSelect}.png')
                img = img.resize((80, 80), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.images[text][color][i] = img

    def _loadImages(self):
        self.images = {}
        colors = ["black", "white"]

        self._loadPieceImage(Pawn.name, colors)
        self._loadPieceImage(Knight.name, colors)
        self._loadPieceImage(King.name, colors)
        self._loadPieceImage(Rock.name, colors)
        self._loadPieceImage(Bishop.name, colors)
        self._loadPieceImage(Queen.name, colors)

        img = Image.open("IMG/figure/empty.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self.images["None"] = ImageTk.PhotoImage(img)
        img = Image.open("IMG/possible.png")
        img = img.resize((80, 80), Image.ANTIALIAS)
        self.images["Possible"] = ImageTk.PhotoImage(img)
        img = Image.open("IMG/back.png")
        img = img.resize((40, 40), Image.ANTIALIAS)
        self.images["Back"] = ImageTk.PhotoImage(img)
        img = Image.open("IMG/resume.png")
        img = img.resize((40, 40), Image.ANTIALIAS)
        self.images["Resume"] = ImageTk.PhotoImage(img)

