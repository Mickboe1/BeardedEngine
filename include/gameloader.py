#!/usr/bin/env python
import re


class GameLoader:
    def __init__(self, main, mr, be, filename):
        self.main = main
        self.mr = mr
        self.be = be

        self.speeds = [[0, 0.1], [50, 3]]  # , [5, 2], [10, 0.2], [22, 5]]
        self.slowBefore = 20

        with open("records/{0}.txt".format(filename), "r") as gamefile:
            for line in gamefile:
                (num, moveWhite, moveBlack) = self.decodeLine(line)
                print num
                self.move(num, moveWhite, True)
                if not moveBlack == "":
                    self.move(num, moveBlack, False)

        # except Exception as e:
        #     print e

    def decodeLine(self, line):
        s = line.strip().split(".")

        checkAdd = 1 if "+" in s[1][:-1] else 0
        numberSplit = re.search("\d", s[1]).start() + 1 + checkAdd

        castle = re.search("O-O", (s[1]))
        if castle and castle.start() == 0:
            castleQ = re.search("O-O-O", (s[1]))
            if castleQ:
                numberSplit = castleQ.end() + checkAdd
            else:
                numberSplit = castle.end() + checkAdd
        return int(s[0]), s[1][:numberSplit], s[1][numberSplit:]

    def move(self, num, annotation, white):
        f, t, c = self.mr.resolve(annotation, white)
        speed = 1
        for s in self.speeds:
            if num > s[0]:
                speed = s[1]
        if not c:
            self.main.moveAndVisualise(f, t, speed, True)
        else:
            self.main.moveAndVisualise(f[0], t[0], 0, True)
            self.main.moveAndVisualise(f[1], t[1], speed, True)
