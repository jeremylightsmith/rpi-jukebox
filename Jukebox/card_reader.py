import struct
import time
import sys
import threading

class CardReader(threading.Thread):
  def __init__(self, bus):
    super(CardReader, self).__init__()
    self.bus = bus
    self.setDaemon(True)

  def run(self):
    self.infile_path = "/dev/input/by-id/usb-Sycreader_RFID_Technology_Co.__Ltd_SYC_ID_IC_USB_Reader_08FF20140315-event-kbd"
    
    #long int, long int, unsigned short, unsigned short, unsigned int
    FORMAT = 'llHHI'
    EVENT_SIZE = struct.calcsize(FORMAT)

    in_file = open(infile_path, "rb")

    event = in_file.read(EVENT_SIZE)

    while event:
        (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

        if type != 0 or code != 0 or value != 0:
            print("Event type %u, code %u, value: %u at %d, %d" % \
                (type, code, value, tv_sec, tv_usec))
        else:
            # Events with code, type and value == 0 are "separator" events
            print("===========================================")

        event = in_file.read(EVENT_SIZE)

    in_file.close()
    # while True:
    #   id = "1234567890"
    #   print("read card " + id)
    #   self.bus.put(["card_read", id])
    #   time.sleep(10)

