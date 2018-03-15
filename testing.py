#!/usr/bin/env python
import unittest
from include.board import Board
from include.piecechecker import PieceChecker


class PieceCheckerTestingClass(unittest.TestCase):
    def test_pawn_validation(self):
        self.board = Board()
        self.pc = PieceChecker(self.board)

        self.board.movePiece("e2", "e4")
        self.board.movePiece("d7", "d5")
        self.board.movePiece("d2", "d3")

        self.assertEqual(self.pc.checkMovesPiece("e4"), ('e4', ['e5', 'd5']))
        self.assertEqual(self.pc.checkMovesPiece("d5"), ('d5', ['d4', 'e4']))
        self.assertEqual(self.pc.checkMovesPiece("d3"), ('d3', ['d4']))
        self.assertEqual(self.pc.checkMovesPiece("a2"), ('a2', ['a3', 'a4']))

    def test_knight_validation(self):
        self.board = Board()
        self.pc = PieceChecker(self.board)

        self.board.movePiece("b1", "a3")
        self.board.movePiece("g1", "f3")
        self.board.movePiece("b8", "c6")
        self.board.movePiece("g8", "f6")
        self.board.movePiece("f3", "e5")

        self.assertEqual(self.pc.checkMovesPiece("f6"), ('f6', ['g8', 'e4', 'g4', 'd5', 'h5']))
        self.assertEqual(self.pc.checkMovesPiece("c6"), ('c6', ['b8', 'b4', 'd4', 'a5', 'e5']))
        self.assertEqual(self.pc.checkMovesPiece("a3"), ('a3', ['b5', 'b1', 'c4']))
        self.assertEqual(self.pc.checkMovesPiece("e5"), ('e5', ['d7', 'f7', 'd3', 'f3', 'c6', 'g6', 'c4', 'g4']))

    def test_rook_validation(self):
        self.board = Board()
        self.pc = PieceChecker(self.board)

        self.board.movePiece("h1", "h2",)
        self.board.movePiece("h2", "h5",)
        self.board.movePiece("h5", "e5",)
        self.board.movePiece("a8", "a7",)
        self.board.movePiece("a7", "a4",)
        self.board.movePiece("a4", "d4",)
        self.board.movePiece("h8", "h7",)
        self.board.movePiece("h7", "h8",)
        self.board.movePiece("a1", "a2",)
        self.board.movePiece("a2", "a8",)

        self.assertEqual(self.pc.checkMovesPiece("e5"), ('e5', ['f5', 'g5', 'h5', 'd5', 'c5', 'b5', 'a5', 'e4', 'e3', 'e6', 'e7']))
        self.assertEqual(self.pc.checkMovesPiece("d4"), ('d4', ['e4', 'f4', 'g4', 'h4', 'c4', 'b4', 'a4', 'd3', 'd2', 'd5', 'd6']))
        self.assertEqual(self.pc.checkMovesPiece("h8"), ('h8', ['h7', 'h6', 'h5', 'h4', 'h3', 'h2', 'h1']))
        self.assertEqual(self.pc.checkMovesPiece("a8"), ('a8', ['b8', 'a7', 'a6', 'a5', 'a4', 'a3', 'a2', 'a1']))

    def test_bishop_validation(self):
        self.board = Board()
        self.pc = PieceChecker(self.board)

        self.board.movePiece("e2", "e4",)
        self.board.movePiece("d2", "d4",)
        self.board.movePiece("c1", "g5",)
        self.board.movePiece("f1", "b5",)
        self.board.movePiece("e7", "e6",)
        self.board.movePiece("d1", "d2",)

        self.assertEqual(self.pc.checkMovesPiece("f8"), ('f8', ['e7', 'd6', 'c5', 'b4', 'a3']))
        self.assertEqual(self.pc.checkMovesPiece("c8"), ('c8', []))
        self.assertEqual(self.pc.checkMovesPiece("b5"), ('b5', ['c4', 'd3', 'e2', 'f1', 'a4', 'c6', 'd7', 'a6']))
        self.assertEqual(self.pc.checkMovesPiece("g5"), ('g5', ['h4', 'f4', 'e3', 'h6', 'f6', 'e7', 'd8']))

    def test_queen_validation(self):
        self.board = Board()
        self.pc = PieceChecker(self.board)

        self.board.movePiece("d1", "e5")
        self.board.movePiece("d8", "g3")
        self.board.movePiece("e1", "c4")

        self.assertEqual(self.pc.checkMovesPiece("e5"), ('e5', ['f4', 'g3', 'd4', 'c3', 'f6', 'g7', 'd6', 'c7', 'f5', 'g5', 'h5', 'd5', 'c5', 'b5', 'a5', 'e4', 'e3', 'e6', 'e7']))
        self.assertEqual(self.pc.checkMovesPiece("g3"), ('g3', ['h2', 'f2', 'h4', 'f4', 'e5', 'h3', 'f3', 'e3', 'd3', 'c3', 'b3', 'a3', 'g2', 'g4', 'g5', 'g6']))

    def test_king_validation(self):
        self.board = Board()
        self.pc = PieceChecker(self.board)

        self.board.movePiece("d1", "e5")
        self.board.movePiece("d8", "g3")
        self.board.movePiece("e1", "c4")

        self.assertEqual(self.pc.checkMovesPiece("c4"), ('c4', ['d3', 'd4', 'd5', 'c3', 'c5', 'b3', 'b4', 'b5']))
        self.assertEqual(self.pc.checkMovesPiece("e8"), ('e8', ['d8']))


class BoardTestingClass(unittest.TestCase):
    def test_chessNotationToXY(self):
        b = Board()
        self.assertEqual(b.chessNotationToXY("e4"), (3, 3))
        self.assertEqual(b.chessNotationToXY("c5"), (5, 4))
        self.assertEqual(b.chessNotationToXY("f2"), (2, 1))

    def test_xyToChessNotation(self):
        b = Board()
        self.assertEqual(b.xyToChessNotation(3, 3), "e4")
        self.assertEqual(b.xyToChessNotation(5, 4), "c5")
        self.assertEqual(b.xyToChessNotation(2, 1), "f2")

    def test_notationToPositionAndBack(self):
        b = Board()
        xe4, ye4 = b.chessNotationToXY("e4")
        xc7, yc7 = b.chessNotationToXY("c7")
        xf2, yf2 = b.chessNotationToXY("f2")

        self.assertEqual(b.xyToChessNotation(xe4, ye4), "e4")
        self.assertEqual(b.xyToChessNotation(xc7, yc7), "c7")
        self.assertEqual(b.xyToChessNotation(xf2, yf2), "f2")

    def test_checkPosition(self):
        b = Board()
        # overide a piece for testing with a not existing piece lets call it T
        b.board[4][0] = "T"  # h5
        self.assertEqual(b.checkPosition("h5"), "T")

    def test_flipBoard(self):
        b = Board()
        # verify by comparing b2 to a flipped g7
        self.assertEqual(b.board[1][1], b.flipBoard()[6][6])


if __name__ == '__main__':
    unittest.main()
