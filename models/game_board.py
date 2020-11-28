from helper.board_position import BoardPosition
from models.piece import Piece, Direction
from models.pieces.pawn import Pawn
from models.pieces.knight import Knight
from models.pieces.king import King
from models.pieces.rock import Rock


class GameBoard:
    _pieceMap = []
    boardSize = [8, 8]

    def __init__(self):
        for x in range(8):
            self._pieceMap.append([])
            for y in range(8):
                if y == 1:
                    self._pieceMap[x].append(
                        Pawn("black", False, Direction.UP))
                elif y == 6:
                    self._pieceMap[x].append(
                        Pawn("white", False, Direction.DOWN))
                elif y == 0:
                    if(x == 1 or x == 6):
                        self._pieceMap[x].append(
                            Knight("black", False))
                    elif x == 4:
                        self._pieceMap[x].append(
                            King("black", True))
                    elif(x == 0 or x == 7):
                        self._pieceMap[x].append(
                            Rock("black", False))
                    else:
                        self._pieceMap[x].append(None)
                elif y == 7:
                    if(x == 1 or x == 6):
                        self._pieceMap[x].append(
                            Knight("white", False))
                    elif x == 4:
                        self._pieceMap[x].append(
                            King("white", True))
                    elif(x == 0 or x == 7):
                        self._pieceMap[x].append(
                            Rock("white", False))
                    else:
                        self._pieceMap[x].append(None)
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

    def _checkIfCheckmate(self, color):
        kingPosList = []
        for x in range(len(self.pieceMap)):
            for y in range(len(self.pieceMap[x])):
                piece = self.pieceMap[x][y]
                if piece is not None and piece.isKing == True and piece.color == color:
                    kingPosList.append(BoardPosition(x, y))

        isCheckmate = False
        for kingPos in kingPosList:
            if self._isThreatenend(kingPos) is True:
                isCheckmate = True
        return isCheckmate

    def _isThreatenend(self, pos, ignoreColor=""):
        isThreatenend = False
        for x in range(len(self.pieceMap)):
            for y in range(len(self.pieceMap[x])):
                piece = self.pieceMap[x][y]
                if(piece is not None):
                    if (ignoreColor == "" or piece.color != ignoreColor) and piece.canMove(self.pieceMap, BoardPosition(
                            x, y), pos):
                        isThreatenend = True
        return isThreatenend

    def movePiece(self, fromPos, toPos):
        piece = self.getPiece(fromPos)
        pieceAtToPos = self.getPiece(toPos)
        if piece is None:
            return False
        if piece.canMove(self.pieceMap, fromPos, toPos):
            self.setPiece(toPos, piece)
            self.setPiece(fromPos, None)
            if self._checkIfCheckmate(piece.color):
                # Wenn Zug als Checkmate erkannt wird, wird er rückgäng gemacht.
                self.setPiece(fromPos, piece)
                self.setPiece(toPos, pieceAtToPos)
                return False
            return True
        specialMove = self.canSpecialMove(fromPos, toPos)
        if len(specialMove) != 0:

            self.setPiece(toPos, self.getPiece(fromPos))
            self.setPiece(fromPos, None)
            self.setPiece(specialMove[1][1], self.getPiece(specialMove[1][0]))
            self.setPiece(specialMove[1][0], None)
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
        isCheckmate = self._checkIfCheckmate(piece.color)
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
        moves = []
        moves += (self._getCastlingMoves())
        return moves

    def canSpecialMove(self, fromPos, toPos):
        moves = self._getSpecialMoves()
        possibleMove = []
        if moves != [[]]:
            for move in moves:
                if move[0] == [fromPos, toPos]:
                    possibleMove = move
                    break
        return possibleMove

    def _getCastlingMove(self, y, rockX):
        king = self.getPiece(BoardPosition(4, y))
        rock = self.getPiece(BoardPosition(rockX, y))
        if king != None and king.name == "king" and rock != None and rock.name == "rock":
            if not self.checkIfSomethingBetween(BoardPosition(4, y), BoardPosition(rockX, y), "y"):
                if rockX == 7:
                    if not self._isThreatenendList([BoardPosition(4, y), BoardPosition(5, y), BoardPosition(6, y)], king.color):
                        return [BoardPosition(4, y), BoardPosition(6, y)], [BoardPosition(rockX, y), BoardPosition(5, y)]
                elif rockX == 0:
                    if not self._isThreatenendList([BoardPosition(4, y), BoardPosition(3, y), BoardPosition(2, y)], king.color):
                        return [BoardPosition(4, y), BoardPosition(2, y)], [BoardPosition(rockX, y), BoardPosition(3, y)]
        return None

    def _getCastlingMoves(self):
        moves = []
        if self._getCastlingMove(0, 7) is not None:
            moves.append(self._getCastlingMove(0, 7))
        if self._getCastlingMove(0, 0) is not None:
            moves.append(self._getCastlingMove(0, 0))
        if self._getCastlingMove(7, 7) is not None:
            moves.append(self._getCastlingMove(7, 7))
        if self._getCastlingMove(7, 0) is not None:
            moves.append(self._getCastlingMove(7, 0))
        return moves

    def _isThreatenendList(self, posList, color=""):
        threatenend = False
        for pos in posList:
            if self._isThreatenend(pos, color):
                threatenend = True
        return threatenend

    def checkIfSomethingBetween(self, pos1, pos2, axis):
        somethingBetween = False
        if(axis == "y"):
            p1 = pos1.X
            p2 = pos2.X
        else:
            p1 = pos1.Y
            p2 = pos2.Y

        if(p1 < p2):
            stepSize = 1
        elif(p1 > p2):
            stepSize = -1
        else:
            return False
        c = p1 + stepSize
        while c != p2:
            if(axis == "y"):
                if self._pieceMap[c][pos1.Y] is not None:
                    somethingBetween = True
            else:
                if self._pieceMap[pos1.X][c] is not None:
                    somethingBetween = True
            c += stepSize
        return somethingBetween

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
