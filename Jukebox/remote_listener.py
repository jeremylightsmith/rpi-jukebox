from keyboard_listener import KeyboardListener

class RemoteListener(KeyboardListener):
  def __init__(self, bus):
    super(RemoteListener, self).__init__("usb-HBGIC_Technology_Co.__Ltd._USB_Keyboard_Mouse-event-kbd")
    self.bus = bus

  # def on_event(self, type, value, code):
  #   if type == 1 and value == 1:
  #     if code == KEY_ENTER:
  #       self.bus.put(["card_read", id])
  #       id = ""

  #     elif code == 11:
  #       id += `0`

  #     else:
  #       id += `code - 1`
