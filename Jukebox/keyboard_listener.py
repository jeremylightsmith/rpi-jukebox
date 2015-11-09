from getch import getch
import threading

class KeyboardListener(threading.Thread):
  def __init__(self, bus):
    super(KeyboardListener, self).__init__()
    self.setDaemon(True)
    self.bus = bus
    self.keys = {
        65: ["first_song"],
        67: ["next_song"],
        66: ["last_song"],
        68: ["previous_song"],
        13: ["play"],
        ord('s'): ["stop"],
        ord('r'): ["repeat"],
        ord('n'): ["no_repeat"],
        ord('q'): ["quit"],
        ord('0'): ["card_read", "0"],
        ord('1'): ["card_read", "1"],
        ord('2'): ["card_read", "2"],
        ord('3'): ["card_read", "3"],
        ord('4'): ["card_read", "4"],
        ord('5'): ["card_read", "5"],
        ord('6'): ["card_read", "6"],
        ord('7'): ["card_read", "7"],
        ord('8'): ["card_read", "8"],
        ord('9'): ["card_read", "9"],
    }

  def run(self):
    while True:
      code = None
      while code == None or code == 27 or code == 91:
        ch = getch()
        code = ord(ch)

      if code in self.keys:
        event = self.keys.get(code)
        self.bus.put(event)
