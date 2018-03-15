#!/usr/bin/env python
from include.board import Board
from include.piecechecker import PieceChecker
from include.gameloader import GameLoader
from include.moveresolver import MoveResolver
from include.boardevaluator import BoardEvaluator
import os
import time


class BeardedEngine:
    def __init__(self):
        self.board = Board()
        self.pc = PieceChecker(self.board)
        self.be = BoardEvaluator(self.pc)
        self.mr = MoveResolver(self.board, self.pc)
        self.gl = GameLoader(self, self.mr, self.be, "simplesteps")

    def moveAndVisualise(self, begin, end, sleeptimer=1, fancy=False):
        self.board.movePiece(begin, end)
        self.clearAndVisualise(sleeptimer, fancy)

    def clearAndVisualise(self, sleeptimer, fancy):
        os.system("clear")

        self.be.Evaluate(self.board)
        self.be.printScore(True)
        if fancy:
            self.board.printBoardStateFancy()
        else:
            self.board.printBoardState()
        time.sleep(sleeptimer)


if __name__ == "__main__":
    pre_run_timer = 1

    os.system("clear")
    os.system("python -m unittest -v testing")
    for i in range(pre_run_timer):
        print "unit test result above, engine starting in {0} seconds".format(
            pre_run_timer - i)
        time.sleep(1)
    os.system("clear")
    # try:
    BeardedEngine()
    # except Exception as e:
    #     print e
