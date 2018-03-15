#!/usr/bin/env python


class PieceChecker:
    def __init__(self, board):
        # overal variables
        self.board = board

        # Piece specific constants
        self.knightMoves = [[1, 2], [-1, 2], [1, -2], [-1, -2],
                            [2, 1], [-2, 1], [2, -1], [-2, -1]]

        self.check = [0, 0]  # w,b
        self.castleAllowed = [[1, 1], [1, 1]]  # w(kq), b(kq)
        self.pieceOptions = {'p': self.pawn,
                             'n': self.knight,
                             'b': self.bishop,
                             'r': self.rook,
                             'q': self.queen,
                             'k': self.king, }

    def checkMovesPiece(self, position):
        p = self.board.checkPosition(position)
        # print position, p
        if not p == " ":
            return self.pieceOptions[p.lower()](position, not p.isupper())
        return " ", []

    def pawn(self, position, white):
        # TODO: En passant rule
        returnPositions = []
        direction = 1 + (-2 * int(not white))
        (x, y) = self.board.chessNotationToXY(position)
        inStartPose = (white and y == 1) or (not white and y == 6)

        # first check non-offensive movement.
        for i in range(0, 1 + int(inStartPose)):
            if not self.board.board[y + (i + 1) * direction][x] == " ":
                break
            returnPositions.append(self.board.xyToChessNotation(x, y + (i + 1) * direction))

        # check take possibility
        if (not x - 1 == -1 and not self.board.board[y + direction][x - 1] == " " and
                self.board.board[y + direction][x - 1].isupper() == white):
            returnPositions.append(self.board.xyToChessNotation(x - 1, y + direction))
        if (not x + 1 == 8 and not self.board.board[y + direction][x + 1] == " " and
                self.board.board[y + direction][x + 1].isupper() == white):
            returnPositions.append(self.board.xyToChessNotation(x + 1, y + direction))

        return position, returnPositions

    def knight(self, position, white):
        returnPositions = []
        (x, y) = self.board.chessNotationToXY(position)

        for move in self.knightMoves:
            if(
                not (x + move[0] < 0 or x + move[0] > 7) and
                not (y + move[1] < 0 or y + move[1] > 7)
            ):
                if (
                    self.board.board[y + move[1]][x + move[0]] == " " or
                    (
                        not self.board.board[y + move[1]][x + move[0]] == " " and
                        self.board.board[y + move[1]][x + move[0]].isupper() == white
                    )
                ):
                    returnPositions.append(self.board.xyToChessNotation(x + move[0], y + move[1]))

        return position, returnPositions

    def rook(self, position, white):
        returnPositions = []
        (x, y) = self.board.chessNotationToXY(position)

        for horizontal in range(0, 2):
            for vertical in range(-1, 2, 2):
                i = 1
                while not (y + (i * vertical * horizontal) < 0 or y + (i * vertical * horizontal) > 7 or
                           x + (i * vertical * int(not horizontal)) < 0 or x + (i * vertical * int(not horizontal)) > 7):
                    if (
                        self.board.board[y + i * vertical * horizontal][x + (i * vertical * int(not horizontal))] == " " or
                        (
                            not self.board.board[y + i * vertical * horizontal][x + (i * vertical * int(not horizontal))] == " " and
                            self.board.board[y + i * vertical * horizontal][x + (i * vertical * int(not horizontal))].isupper() == white
                        )
                    ):
                        returnPositions.append(self.board.xyToChessNotation(x + (i * vertical * int(not horizontal)), y + i * vertical * horizontal))
                        if self.board.board[y + i * vertical * horizontal][x + (i * vertical * int(not horizontal))] != " ":
                            break
                    else:
                        break
                    i += 1
        return position, returnPositions

    def bishop(self, position, white):
        returnPositions = []
        (x, y) = self.board.chessNotationToXY(position)

        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                d = 1
                while not ((y + i * d) < 0 or(y + i * d) > 7 or (x + j * d) < 0 or (x + j * d) > 7):
                    if self.board.board[y + i * d][x + j * d] == " " or (
                        not self.board.board[y + i * d][x + j * d] == " " and
                        self.board.board[y + i * d][x + j * d].isupper() == white
                    ):
                        returnPositions.append(self.board.xyToChessNotation(x + j * d, y + i * d))
                        if self.board.board[y + i * d][x + j * d] != " ":
                            break
                    else:
                        break
                    d += 1

        return position, returnPositions

    def queen(self, position, white):
        returnPositions = []
        (x, y) = self.board.chessNotationToXY(position)

        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                d = 1
                while not ((y + i * d) < 0 or(y + i * d) > 7 or (x + j * d) < 0 or (x + j * d) > 7):
                    if self.board.board[y + i * d][x + j * d] == " " or (
                        not self.board.board[y + i * d][x + j * d] == " " and
                        self.board.board[y + i * d][x + j * d].isupper() == white
                    ):
                        returnPositions.append(self.board.xyToChessNotation(x + j * d, y + i * d))
                        if self.board.board[y + i * d][x + j * d] != " ":
                            break
                    else:
                        break
                    d += 1

        for horizontal in range(0, 2):
            for vertical in range(-1, 2, 2):
                i = 1
                while not (y + (i * vertical * horizontal) < 0 or y + (i * vertical * horizontal) > 7 or
                           x + (i * vertical * int(not horizontal)) < 0 or x + (i * vertical * int(not horizontal)) > 7):
                    if (
                        self.board.board[y + i * vertical * horizontal][x + (i * vertical * int(not horizontal))] == " " or
                        (
                            not self.board.board[y + i * vertical * horizontal][x + (i * vertical * int(not horizontal))] == " " and
                            self.board.board[y + i * vertical * horizontal][x + (i * vertical * int(not horizontal))].isupper() == white
                        )
                    ):
                        returnPositions.append(self.board.xyToChessNotation(x + (i * vertical * int(not horizontal)), y + i * vertical * horizontal))
                        if self.board.board[y + i * vertical * horizontal][x + (i * vertical * int(not horizontal))] != " ":
                            break
                    else:
                        break
                    i += 1

        return position, returnPositions

    def king(self, position, white):
        # TODO: king check
        returnPositions = []
        (x, y) = self.board.chessNotationToXY(position)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (x + i < 0 or x + i > 7 or y + j < 0 or y + j > 7) and not(i == 0 and j == 0):
                    if (
                        self.board.board[y + j][x + i] == " " or
                        (
                            not self.board.board[y + j][x + i] == " " and
                            self.board.board[y + j][x + i].isupper() == white
                        )
                    ):
                        returnPositions.append(self.board.xyToChessNotation(x + i, y + j))

        return position, returnPositions
