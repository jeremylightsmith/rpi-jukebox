# Jeremy's Jukebox 2.0
# Author: Jeremy Lightsmith
# Copyright (c) 2015 Jeremy Lightsmith

from getch import getch

class KeyboardReader:
    CONTEXT_MENU = 16

    def __init__(self):
        self.keys = {
            65: ["up"],
            67: ["right"],
            66: ["down"],
            68: ["left"],
            13: ["enter"],
            ord('q'): ["quit"],
            ord('0'): ["card", 0],
            ord('1'): ["card", 1],
            ord('2'): ["card", 2],
            ord('3'): ["card", 3],
            ord('4'): ["card", 4],
            ord('5'): ["card", 5],
            ord('6'): ["card", 6],
            ord('7'): ["card", 7],
            ord('8'): ["card", 8],
            ord('9'): ["card", 9],
        }

    def read(self):
        code = None
        while code == None or code == 27 or code == 91:
            ch = getch()
            code = ord(ch)

        event = self.keys.get(code, ["unknown"])

        if event == ["unknown"]:
            print "unknown key code = %i" % code

        return event