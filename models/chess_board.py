from models.game_board import GameBoard


from models.piece import Piece, Direction
from models.pieces.pawn import Pawn
from models.pieces.knight import Knight
from models.pieces.king import King
from models.pieces.rock import Rock
from models.pieces.queen import Queen
from models.pieces.bishop import Bishop

class ChessBoard(GameBoard):

    def __init__(self, color1, color2):
        super().__init__(self._createPieceList2D(color1, color2))

    def _createPieceList2D(self, player1Color: str, player2Color: str):
        pieceList2D = []
        for x in range(8):
            pieceList2D.append([])
            for y in range(8):
                if y == 1:
                    pieceList2D[x].append(
                        Pawn(player1Color, False, Direction.UP))
                elif y == 6:
                    pieceList2D[x].append(
                        Pawn(player2Color, False, Direction.DOWN))
                elif y == 0:
                    if(x == 1 or x == 6):
                        pieceList2D[x].append(
                            Knight(player1Color, False))
                    elif x == 4:
                        pieceList2D[x].append(
                            King(player1Color, True))
                    elif x == 3:
                        pieceList2D[x].append(
                            Queen(player1Color, False))
                    elif x == 2 or x == 5:
                        pieceList2D[x].append(
                            Bishop(player1Color, False))
                    elif(x == 0 or x == 7):
                        pieceList2D[x].append(
                            Rock(player1Color, False))
                    else:
                        pieceList2D[x].append(None)
                elif y == 7:
                    if(x == 1 or x == 6):
                        pieceList2D[x].append(
                            Knight(player2Color, False))
                    elif x == 4:
                        pieceList2D[x].append(
                            King(player2Color, True))
                    elif x == 3:
                        pieceList2D[x].append(
                            Queen(player2Color, False))
                    elif x == 2 or x == 5:
                        pieceList2D[x].append(
                            Bishop(player2Color, False))
                    elif(x == 0 or x == 7):
                        pieceList2D[x].append(
                            Rock(player2Color, False))
                    else:
                        pieceList2D[x].append(None)
                else:
                    pieceList2D[x].append(None)
        return pieceList2D

