from helper.board_position import BoardPosition
from models.piece import Piece, Direction
from models.pieces.pawn import Pawn
from models.pieces.knight import Knight


class GameBoard:
    _pieceMap = []
    boardSize = [8, 8]

    def __init__(self):
        for x in range(8):
            self._pieceMap.append([])
            for y in range(8):
                if y is 1:
                    self._pieceMap[x].append(
                        Pawn("white", False, Direction.UP))
                elif y is 6:
                    self._pieceMap[x].append(
                        Pawn("black", False, Direction.DOWN))
                elif y is 0:
                    self._pieceMap[x].append(
                        Knight("white", False, Direction.UP))
                else:
                    self._pieceMap[x].append(None)

    def printMap(self):
        for y in range(self.boardSize[1]):
            textLine = ""
            for x in range(self.boardSize[0]):
                piece = self.pieceMap[x][y]
                if self.pieceMap[x][y] is None:
                    textLine += "X "
                else:
                    textLine += piece.text + " "
            print(textLine)

    def _isCheckmate(self):
        kingPosList = []
        for x in range(len(self.pieceMap)):
            for y in range(len(self.pieceMap[x])):
                piece = self.pieceMap[x][y]
                if piece is not None and piece.isKing == True:
                    kingPosList.append(BoardPosition(x, y))

        isCheckmate = False
        for kingPos in kingPosList:
            if self._isThreatenend(kingPos) is True:
                isCheckmate = True
        return isCheckmate

    def _isThreatenend(self, pos):
        isThreatenend = False
        for x in range(len(self.pieceMap)):
            for y in range(len(self.pieceMap[x])):
                piece = self.pieceMap[x][y]
                isThreatenend = piece.canMove(self.pieceMap, BoardPosition(
                    x, y), pos)
        return isThreatenend

    def movePiece(self, fromPos, toPos):
        piece = self.getPiece(fromPos)
        pieceAtToPos = self.getPiece(toPos)
        if piece is None:
            return False
        if piece.canMove(self.pieceMap, fromPos, toPos):
            self.setPiece(toPos, piece)
            self.setPiece(fromPos, None)
            if not self._isCheckmate:
                # Wenn Zug als Checkmate erkannt wird, wird er rückgäng gemacht.
                self.setPiece(fromPos, piece)
                self.setPiece(toPos, pieceAtToPos)
                return False
            return True
        else:
            return False

    def getAllPossibleMoves(self, color):
        piecePosList = self._getPiecePositionsWithColor(color)
        allPossibleMoves = []
        for piecePos in piecePosList:
            possibleMovePos = self.getAllPossibleMovePosOfPiece(piecePos)
            for move in possibleMovePos:
                allPossibleMoves.append([piecePos, move])
        return allPossibleMoves

    def getAllPossibleMovePosOfPiece(self, piecePos):
        piece = self.getPiece(piecePos)
        movePosList = piece.allPossibleMoves(self.pieceMap, piecePos)

        possibleMovePos = []
        for movePos in movePosList:
            if self._isMoveCheckmate(piecePos, movePos) is False:
                possibleMovePos.append(movePos)
        return possibleMovePos

    def _isMoveCheckmate(self, fromPos, toPos):
        piece = self.getPiece(fromPos)
        pieceAtToPos = self.getPiece(toPos)

        self.setPiece(toPos, piece)
        self.setPiece(fromPos, None)
        isCheckmate = self._isCheckmate()
        self.setPiece(fromPos, piece)
        self.setPiece(toPos, pieceAtToPos)
        return isCheckmate

    def changePiece(self, pos: BoardPosition, toPiece: Piece):
        print("")

    def getPiece(self, pos: BoardPosition):
        return self.pieceMap[pos.X][pos.Y]

    def _getPiecePositionsWithColor(self, color):
        piecePosWithColorList = []
        for x in range(len(self._pieceMap)):
            for y in range(len(self._pieceMap)):
                piece = self._pieceMap[x][y]
                if piece is not None and piece.color is color:
                    piecePosWithColorList.append(BoardPosition(x, y))
        return piecePosWithColorList

    # Return castling move, wenn dieser möglich ist
    def _getSpecialMoves(self):
        return

    def _getSpecialMovesOfPiece(self, pos):
        piece = self.getPiece(pos)
        if piece.isKing:
            print()

    def setPiece(self, boardPosition, piece):
        self._pieceMap[boardPosition.X][boardPosition.Y] = piece

    def canColorMove(self, color):
        return self.getAllPossibleMoves(color) != []

    @ property
    def pieceMap(self):
        return self._pieceMap[:]
