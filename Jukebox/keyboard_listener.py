import struct
import time
import sys
import threading

class KeyboardListener(threading.Thread):
  def __init__(self, device_id):
    super(KeyboardListener, self).__init__()
    self.device_id = device_id
    self.setDaemon(True)
    print "init Keyboard Listener to ", device_id

  def on_event(self, type, value, code):
    print "on_event(", type, ", ", value, ", ", code, ")"

  def run(self):
    infile_path = "/dev/input/by-id/" + self.device_id
    
    #long int, long int, unsigned short, unsigned short, unsigned int
    FORMAT = 'llHHI'
    EVENT_SIZE = struct.calcsize(FORMAT)

    in_file = open(infile_path, "rb")

    event = in_file.read(EVENT_SIZE)
    id = ""

    while event:
      (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

      self.on_event(type, value, code)

      event = in_file.read(EVENT_SIZE)

    in_file.close()
