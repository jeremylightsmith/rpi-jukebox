from dev_input_listener import DevInputListener

CODE_TO_EVENTS = {
  116: "stop",
  106: "next_song",
  105: "previous_song",
  1: "toggle_repeating", 
  # 127: "no_repeat", context menu
  103: "first_song",
  108: "last_song",


  114: "volume_down",
  115: "volume_up",

  28: "play",
  172: "home"
}

class RemoteListener(DevInputListener):
  def __init__(self, bus):
    # super(RemoteListener, self).__init__("usb-HBGIC_Technology_Co.__Ltd._USB_Keyboard_Mouse-event-kbd")
    super(RemoteListener, self).__init__("usb-Sycreader_RFID_Technology_Co.__Ltd_SYC_ID_IC_USB_Reader_08FF20140315-event-kbd")
    self.bus = bus


  def on_event(self, type, value, code):
    if type == 1 and value == 1:
      if code in CODE_TO_EVENTS:
        self.bus.put([CODE_TO_EVENTS[code]])
