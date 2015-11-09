from keyboard_listener import KeyboardListener

KEY_ENTER = 28

class CardReader(KeyboardListener):
  def __init__(self, bus):
    super(CardReader, self).__init__("usb-Sycreader_RFID_Technology_Co.__Ltd_SYC_ID_IC_USB_Reader_08FF20140315-event-kbd")
    self.bus = bus
    self.id = ""

  def on_event(self, type, value, code):
    if type == 1 and value == 1:
      if code == KEY_ENTER:
        self.bus.put(["card_read", self.id])
        self.id = ""

      elif code == 11:
        self.id += `0`

      else:
        self.id += `code - 1`

