from helper.board_position import BoardPosition, BoardChange, BoardMove
from models.piece import Piece, Direction
from typing import Union


class GameBoard:

    def __init__(self, pieceList2D: list[list[Piece]]):
        self._pieceMap = pieceList2D

    @property
    def boardSize(self):
        return [len(self._pieceMap), len(self._pieceMap[0])]

    def getPiece(self, pos: BoardPosition):
        return self.pieceMap[pos.X][pos.Y]

    def setPiece(self, boardPosition, piece):
        self._pieceMap[boardPosition.X][boardPosition.Y] = piece

    @ property
    def pieceMap(self):
        return self._pieceMap[:]

    def movePiece(self, fromPos: BoardPosition, toPos: BoardPosition) -> bool:
        move = self.getValidMove(fromPos, toPos)
        if move is not None:
            self.executeChange(move.triggerChange)
            for change in move.otherChanges:
                self.executeChange(change)
            return True
        return False

    def executeChange(self, change: BoardChange):
        self.setPiece(change.toPos, self.getPiece(change.fromPos))
        self.setPiece(change.fromPos, None)

    def promotePiece(self, piecePos: BoardPosition, piece: Piece):
        # Piece auf piecePos wird mit anderen Piece, abhängig von promoteName ersetzt
        oldPiece = self.getPiece(piecePos)
        self.setPiece(piecePos, piece)

    def canPromote(self, pos):
        # checkt abhängig vom Piece Type, ob das Piece promote werden darf
        piece = self.getPiece(pos)
        if piece is None:
            return False

        if piece.canPromote(self.pieceMap, pos):
            return True
        else:
            return False

    def canColorMove(self, color):
        return self.getValidMovesByColor(color) != []

    def isInCheck(self, color: str) -> bool:
        kingPosList = []
        for x in range(len(self.pieceMap)):
            for y in range(len(self.pieceMap[x])):
                piece = self.pieceMap[x][y]
                if piece is not None and piece.isKing == True and piece.color == color:
                    kingPosList.append(BoardPosition(x, y))

        isInCheck = False
        for kingPos in kingPosList:
            if self._canBeTaken(kingPos) is True:
                isInCheck = True
        return isInCheck

    def _isMoveCheck(self, move: BoardMove) -> bool:
        fromPos = move.triggerChange.fromPos
        toPos = move.triggerChange.toPos

        piece = self.getPiece(move.triggerChange.fromPos)
        pieceAtToPos = self.getPiece(move.triggerChange.toPos)

        if piece == None:
            return False

        self.setPiece(toPos, piece)
        self.setPiece(fromPos, None)
        isCheck = self.isInCheck(piece.color)
        self.setPiece(fromPos, piece)
        self.setPiece(toPos, pieceAtToPos)
        return isCheck

    def _canBeTaken(self, pos: BoardPosition, ignoreColor=""):
        # Gibt True aus, wenn es von irgendeinen anderen Piece angegriffen wird, außer von Pieces mit ignoreColor
        isThreatenend = False
        for x in range(len(self.pieceMap)):
            for y in range(len(self.pieceMap[x])):
                piece = self.pieceMap[x][y]
                if(piece is not None):
                    if (ignoreColor == "" or piece.color != ignoreColor) and piece.canMove(self.pieceMap, BoardPosition(
                            x, y), pos):
                        isThreatenend = True
        return isThreatenend

    def isStalemate(self, color: str) -> bool:
        # Gibt True aus, wenn keine Piece mit color sich bewegen können, aber der König nicht attackiert wird
        if self.canColorMove(color):
            return False

        if self.isInCheck(color):
            return False
        return True

    def getValidMove(self, piecePos, toPos) -> BoardMove:
        moves = self.getValidMoves(piecePos)

        for move in moves:
            if move.triggerChange.fromPos == piecePos and move.triggerChange.toPos == toPos:
                return move
        return None

    def getValidMoves(self, piecePos) -> list[BoardMove]:
        piece = self.getPiece(piecePos)
        if piece is None:
            return []

        moves = []

        moves += self.getUsualMoves(piecePos)
        moves += self.getOddMoves(piecePos)

        return moves

    def getValidMovesByColor(self, color) -> list[BoardMove]:
        piecePos = self._getAllPiecePosOfColor(color)
        moves = []
        for pos in piecePos:
            moves += self.getValidMoves(pos)
        return moves

    def getUsualMove(self, piecePos, toPos) -> list[BoardMove]:
        moves = self.getUsualMoves(piecePos)

        for move in moves:
            if move.triggerMove.fromPos == piecePos and move.triggerMove.toPos == toPos:
                return move
        return []

    def getUsualMoves(self, piecePos) -> list[BoardMove]:
        piece = self.getPiece(piecePos)
        if piece is None:
            return []

        moves = piece.allMoves(self.pieceMap, piecePos)
        validMoves = []

        for move in moves:
            if self._isMoveCheck(move) is False:
                validMoves.append(move)
        return validMoves

    def _getAllPiecePosOfColor(self, color):
        piecePos = []
        for x in range(len(self._pieceMap)):
            for y in range(len(self._pieceMap)):
                piece = self._pieceMap[x][y]
                if piece is not None and piece.color is color:
                    piecePos.append(BoardPosition(x, y))
        return piecePos

    def getOddMoves(self, piecePos) -> list[BoardMove]:
        moves = []
        moves += self._getCastlingMoves(piecePos)
        return moves

    def canOddMove(self, piecePos) -> bool:
        moves = self.getOddMoves(piecePos)
        canMove = False
        for move in moves:
            if move[0] == piecePos:
                canMove = True
                break
        return canMove

    def _getCastlingMoves(self, piecePos):
        castlingMoves = self._getAllCastlingMoves()
        moves = []
        for move in castlingMoves:
            if move.triggerChange.fromPos== piecePos:
                moves.append(move)
        return moves

    def _getAllCastlingMoves(self) -> list[BoardMove]:
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

    def _getCastlingMove(self, y, rockX) -> BoardMove:
        king = self.getPiece(BoardPosition(4, y))
        rock = self.getPiece(BoardPosition(rockX, y))
        if king != None and king.name == "king" and rock != None and rock.name == "rock":
            if not self.checkIfSomethingBetween(BoardPosition(4, y), BoardPosition(rockX, y), "y"):
                if rockX == 7:
                    if not self._canAnyBeTaken([BoardPosition(4, y), BoardPosition(5, y), BoardPosition(6, y)], king.color):
                        triggerChange = BoardChange(
                            BoardPosition(4, y), BoardPosition(6, y))
                        otherChange = BoardChange(
                            BoardPosition(rockX, y), BoardPosition(5, y))
                        boardMove = BoardMove(triggerChange, otherChange)
                        return boardMove
                elif rockX == 0:
                    if not self._canAnyBeTaken([BoardPosition(4, y), BoardPosition(3, y), BoardPosition(2, y)], king.color):
                        triggerChange = BoardChange(
                            BoardPosition(4, y), BoardPosition(2, y))
                        otherChange = BoardChange(
                            BoardPosition(rockX, y), BoardPosition(3, y))
                        boardMove = BoardMove(triggerChange, otherChange)
                        return boardMove
        return None

    def _canAnyBeTaken(self, posList, ignoreColor=""):
        threatenend = False
        for pos in posList:
            if self._canBeTaken(pos, ignoreColor):
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
