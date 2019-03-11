#!/usr/bin/env python


class MoveResolver:
    def __init__(self, board, pc):
        self.pc = pc

    def resolve(self, annotation, white, board):
        annotation = annotation.split("+")[0]
        if "O-O-O" in annotation:
            row = str(1 + 7 * int(not white))
            return ["e" + row, "a" + row], ["c" + row, "d" + row], True
        elif "O-O" in annotation:
            row = str(1 + 7 * int(not white))
            return ["e" + row, "h" + row], ["g" + row, "f" + row], True
        else:
            if not annotation[:1].isupper():  # pawn movement
                direction = -1 + 2 * int(not white)
                if not ("x" in annotation):
                    # print annotation, white
                    for i in range(1, 3):
                        new_annotation = annotation[:1] + \
                            str(int(annotation[1:]) + i * direction)
                        if not board.checkPosition(new_annotation) == " ":
                            return new_annotation, annotation, False
                else:
                    collumn_from = annotation[:1]
                    row_from = int(annotation[-1:])

                    return collumn_from + str(row_from + direction), annotation[2:], False

            else:
                p = annotation[:1]
                take = 0
                frm = ""
                if ("x" in annotation):
                    take = 1
                if len(annotation) > 3 + take:
                    frm = annotation[1 + take:2 + take]
                    # print frm
                # print (self.board.whitePieces if white else self.board.blackPieces)
                for piece in (board.whitePieces if white else board.blackPieces):
                    if piece[0] == p or piece[0].upper() == p and (frm == "" or frm in piece[1]):
                        (new_annotation, options) = self.pc.checkMovesPiece(
                            piece[1], board)
                        # print new_annotation, options
                        # print self.board.blackPieces
                        if annotation[1 + take + (0 if frm == "" else 1):] in options:
                            return new_annotation, annotation[1 + take + (0 if frm == "" else 1):], False
        return '', '', False
