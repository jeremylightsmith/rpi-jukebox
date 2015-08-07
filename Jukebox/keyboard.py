import sys
from getch import getch

class KeyboardReader:
    UP = 65
    RIGHT = 67
    DOWN = 66
    LEFT = 68
    ENTER = 13
    CONTEXT_MENU = 16

    def read(self):
        code = None
        while code == None or code == 27 or code == 91:
            ch = getch()
            code = ord(ch)

        if ch == 'q':
            sys.exit()
        
        elif ord('0') <= code and code <= ord('9'):
            # print "found a number! - %i" % (code - ord('0'))
            return code - ord('0')

        print "code = %i" % code

        return code