from models.game_board import GameBoard
from helper.board_position import BoardPosition


class BoardState:
    def __init__(self, gameBoard: GameBoard, selectedPiecePos):
        self.map = []
        selectedPiece = None
        if selectedPiecePos is not None:
            selectedPiece = gameBoard.getPiece(selectedPiecePos)
        for x in range(gameBoard.boardSize[0]):
            self.map.append([])
            for y in range(gameBoard.boardSize[1]):
                pos = BoardPosition(x, y)
                piece = gameBoard.getPiece(pos)
                if piece is not None:
                    content = piece.name
                    color = piece.color
                else:
                    content = "None"
                    color = "None"
                self.map[x].append(FieldState(content, color))
                if selectedPiecePos == pos:
                    self.map[x][y].isSelected = True
                elif selectedPiece is not None:
                    self.map[x][y].isPossible = selectedPiece.canMove(
                        gameBoard.pieceMap, selectedPiecePos, pos)


class FieldState:
    def __init__(self, pieceName, pieceColor):
        self.piece = pieceName
        self.color = pieceColor
        self.isSelected = False
        self.isPossible = False
