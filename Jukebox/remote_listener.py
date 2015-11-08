import struct
import time
import sys
import threading

class RemoteListener(threading.Thread):
  def __init__(self, bus):
    super(RemoteListener, self).__init__()
    self.bus = bus
    self.setDaemon(True)


  def run(self):
    while True:
      print("next")
      self.bus.put(["next"])
      time.sleep(17)

