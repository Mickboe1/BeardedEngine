#!/usr/bin/env python
from operator import xor
import copy
import time


class Ai:
    def __init__(self, main, board, be, mr, pc):
        self.main = main
        self.board = board
        self.be = be
        self.mr = mr
        self.pc = pc

        self.player = 'w'
        self.maxDepth = 0

        self.gameloop()

    def gameloop(self):
        self.main.clearAndVisualise(0, True)
        while not self.board.mate:
            if self.player == 'w':
                self.playerMove()
                self.aiMove()
            else:
                pass  # TODO:when players are not white.

    def playerMove(self):
        valid_input = False
        while not valid_input:
            try:
                print('Please make a valid move:')
                inpMove = raw_input()
                f, t, c = self.mr.resolve(inpMove, True, self.board)
                if f != '' and not t == '':
                    valid_input = True
                else:
                    self.main.clearAndVisualise(1, True)
                    print('Invalid move')
            except Exception as e:
                self.main.clearAndVisualise(1, True)
                print('Invalid move')

        self.main.moveAndVisualise(f, t, 1, True)

    def aiMove(self):
        move = self.findBestMove(self.maxDepth, False, self.board, False)
        print move
        self.main.moveAndVisualise(move[0][0], move[0][1], 1, True)

    def findBestMove(self, prev_depth, white, prev_board, prev_offturn_flagg, prev_score=0):
        min_max_flag = xor(white, prev_offturn_flagg)
        best_move = [None, 9999 * (-1 if min_max_flag else 1)]

        for move in self.getMovesForBoard(prev_board, min_max_flag):
            board = copy.deepcopy(prev_board)
            depth = copy.deepcopy(prev_depth)
            offturn_flagg = copy.deepcopy(prev_offturn_flagg)
            score = 0
            board.movePiece(move[0], move[1])
            curr_score = self.be.Evaluate(board)

            if not (depth == 0 and offturn_flagg == True):
                if offturn_flagg:
                    depth -= 1
                    offturn_flagg = False
                else:
                    offturn_flagg = True
                score = self.findBestMove(
                    depth, white, board, offturn_flagg)[1]
            else:
                score = self.be.Evaluate(board)

            if (white and ((not min_max_flag and score > best_move[1]) or (min_max_flag and score < best_move[1]))
                    or (not white and ((not min_max_flag and score < best_move[1]) or (min_max_flag and score > best_move[1])))):
                if not score == 9999:
                    best_move[0] = move
                    best_move[1] = score

        return best_move

    def getMovesForBoard(self, board, white):
        pm = []
        for p in (board.whitePieces if white else board.blackPieces):
            moves = self.pc.checkMovesPiece(p[1], board)
            if len(moves) > 0:
                for move in moves[1]:
                    pm.append([moves[0], move])
                    # pm.append(
                    # ("" if (p[0] == "P" or p[0] == "p") else p[0].upper()) + (move))
        return pm
