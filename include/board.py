#!/usr/bin/env python
class Board:
    def __init__(self):
        self.board = []
        self.whitePieces = []
        self.blackPieces = []

        self.generateSqaures()
        self.setupPieces()

        for j in range(8):
            for i in range(8):
                if not self.board[j][i] == " ":
                    if self.board[j][i].isupper():
                        self.blackPieces.append([self.board[j][i], self.xyToChessNotation(i, j)])
                    else:
                        self.whitePieces.append([self.board[j][i], self.xyToChessNotation(i, j)])

    def generateSqaures(self):
        self.board = [[' ' for y in range(8)] for x in range(8)]

    def setupPieces(self):
        self.board = self.putPiecesOnTheBoard(self.board,
                                              self.generatePieces())
        newBoard = self.putPiecesOnTheBoard(self.flipBoard(),
                                            self.generatePieces('b'))
        self.board = list(reversed(newBoard))

    def putPiecesOnTheBoard(self, board, pieces):
        return pieces + board[2:]

    def generatePieces(self, colour="w"):
        rnb = ['r', 'n', 'b']
        kq = ['q', 'k']
        pawn = 'p'
        if colour == 'b':
            kq = [x.upper() for x in reversed(kq)]
            rnb = [x.upper() for x in rnb]
            pawn = pawn.upper()

        return [rnb + kq + list(reversed(rnb)), [pawn for y in range(8)]]

    # Piece Manipulation
    def chessNotationToXY(self, position):
        return 7 - (ord(position[:1]) - 97), int(position[1:]) - 1

    def xyToChessNotation(self, x, y):
        return str(unichr(97 + (7 - x))) + str(y + 1)

    def checkPositionXY(self, x, y):
        return self.board[y][x]

    def checkPosition(self, position):
        (x, y) = self.chessNotationToXY(position)
        return self.checkPositionXY(x, y)

    def movePiece(self, f, t):
        (yf, xf) = self.chessNotationToXY(f)
        (yt, xt) = self.chessNotationToXY(t)

        if not self.board[xt][yt] == " ":
            position = self.xyToChessNotation(yt, xt)
            for piece in (self.whitePieces if not self.board[xt][yt].isupper() else self.blackPieces):
                if position == piece[1]:
                    (self.whitePieces if not self.board[xt][yt].isupper() else self.blackPieces).remove(piece)

        for p in (self.whitePieces if not self.board[xf][yf].isupper() else self.blackPieces):
            if p[1] == f:
                p[1] = t

        self.board[xt][yt] = self.board[xf][yf]
        self.board[xf][yf] = ' '

    # Board manipulation
    def flipBoard(self):
        """returns a flipped """
        return [list(reversed(x)) for x in reversed(self.board)]

    def printBoardState(self, side="w"):
        # done because the self.board can not be given as a default parameter
        b = self.flipBoard() if side == 'w' else self.board

        print " ---------------------------------"
        ri = 9
        for row in b:
            ri -= 1
            r = "{0}| ".format(ri)
            for i in range(0, len(row)):
                r += row[i] + " | "
            print r
            print " ---------------------------------"
        print "   a   b   c   d   e   f   g   h"

    def printBoardStateFancy(self, side='w'):
        horizontalAnnotation = '     A       B       C       D       E       F       G       H'
        boardDefiderRow = '  ------- ------- ------- ------- ------- ------- ------- -------'
        emptyPlaces = ['       ', ' . . . ']
        pieces = ['P', 'N', 'B', 'R', 'Q', 'K', 'p', 'n', 'b', 'r', 'q', 'k']
        piecesVisualization = ['   _     ( )    /_\  ',
                               '  %~\   `\')(    <__> ',
                               '  .O.    \ /    /_\  ',
                               ' [___]   [ ]   /___\ ',
                               ' \o^o/   [ ]   /___\ ',
                               ' __+__  `. .\'  /___\ ',
                               '   _     (@)    d@b  ',
                               '  %~b   `\'dX    d@@b ',
                               '  .@.    @@@   ./A\. ',
                               ' @___@   @@@   d@@@b ',
                               ' \o*o/   @@@   d@@@b ',
                               ' __+__  `@@@\'  d@@@b ']

        # done because the self.board can not be given as a default parameter
        b = self.flipBoard() if side == 'w' else self.board

        print horizontalAnnotation, '\n', boardDefiderRow
        ri = 8
        for row in b:
            for i in range(0, 3):
                r = str(ri) + "|" if i == 1 else " |"

                for j in range(0, len(row)):
                    if row[j] == " ":
                        r += emptyPlaces[(ri + j) % 2]
                    else:
                        for k in range(0, len(pieces)):
                            if pieces[k] == row[j]:
                                r += str(piecesVisualization[k])[7 * i:7 * (i + 1)]
                    r += '|'
                print r + str(ri) if i == 1 else r
            print boardDefiderRow
            ri -= 1
        print horizontalAnnotation
