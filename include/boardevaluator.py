#!/usr/bin/env python
class BoardEvaluator:
    def __init__(self, pc):
        self.pc = pc

        self.score = 0
        self.displayLimit = 15

        # constants
        self.pieces = ['p', 'n', 'b', 'r', 'q', 'k']
        self.pieceValues = [1, 3, 3, 5, 9, 200]
        self.squareLetter = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def Evaluate(self, board):
        w = 0
        b = 0
        fb = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        # DOUBLE PAWN AND ISOLATED
        for side in [True, False]:
            pm = 0
            penalty = 0
            material = 0
            for p in (board.whitePieces if side else board.blackPieces):
                # POSSIBLE MOVES
                pm += len(self.pc.checkMovesPiece(p[1])[1])

                # MATERIAL
                material += self.pieceValues[self.pieces.index(p[0].lower())] if not p[0].lower() == "k" else 0
                if p[0].lower() == "p" and not int(p[1][1:]) == 7 and not board.checkPosition(p[1][:1] + str(int(p[1][1:]) + 1)) == " ":
                    fb[int(not side)][0] += 1  # TODO fix
                    penalty += 1

            occupied = [pawn[1][:1] for pawn in (board.whitePieces if side else board.blackPieces) if pawn[0].lower() == "p"]
            occupied_count = [occupied.count(self.squareLetter[i]) for i in range(8)]
            penalty += sum([x - 1 for x in occupied_count if x > 1])
            fb[int(not side)][1] = penalty - fb[int(not side)][0]
            # print occupied_count, occupied
            #
            isolated_count = [0 for i in range(8)]
            for i in range(len(occupied_count)):
                for direction in [-1, 1]:
                    if not i + direction < 0 and not i + direction > 7:
                        isolated_count[i] += 1 if occupied_count[i + direction] > 0 else 0
            penalty += sum(occupied_count[i] for i in occupied_count if occupied_count[i] > 0 and isolated_count == 0)
            fb[int(not side)][2] = penalty - fb[int(not side)][1]
            # # print "{3} blocked: {0}  double: {1}  isolated: {2}".format(fb[int(not side)][0], fb[int(not side)][1], fb[int(not side)][2], "white" if side else "black")

            fb[int(not side)][3] = pm
            fb[int(not side)][4] = material

            if side:
                w += (pm * 0.1) - (penalty * 0.5) + material
            else:
                b += (pm * 0.1) - (penalty * 0.5) + material
        print fb

        self.score = b - w

    def printScore(self, fancy=False):
        line = ""
        for i in range(35 - len(str(self.score))):
            line += " "
        print line + str(self.score)

        sep = int((15 + self.score) * 2)
        if sep < 0:
            sep = 0
        if sep > 60:
            sep = 60
        line = "->|"
        for i in range(61):
            line += " " if i <= sep else "|"
        print line + "|<-"
