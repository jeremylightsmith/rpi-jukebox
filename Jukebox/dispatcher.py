import time
from music import MusicPlayer
from card_store import CardStore

class Dispatcher:
  def __init__(self, bus, datadir):
    self.bus = bus
    self.player = MusicPlayer(datadir, bus)
    self.store = CardStore(datadir)

  def card_read(self, id):
    index = self.store.index_of(id)
    if index == 0:
      self.stop()
    elif index == 1:
      self.toggle_repeating()
    else:
      print "playing song ", index
      self.player.play_song(index - 1)
  
  def stop(self):
    self.player.stop_song()

  def toggle_repeating(self):
    self.player.toggle_repeating()
  
  def next_song(self):
    self.player.next_song()
  
  def first_song(self):
    self.player.first_song()
  
  def last_song(self):
    self.player.last_song()
  
  def previous_song(self):
    self.player.previous_song()

  def finished_song(self):
    self.player.finished_song()

  def play(self):
    print "play"
  
  def quit(self):
    self.player.stop_song()
    exit(0)

  def dispatch(self, event):
    handler = getattr(self, event[0], None)
    if handler is None:
      print "Couldn't find handler for ", event[0]
    else:
      handler(*event[1:])

  def start(self):
    while True:
      while not self.bus.empty():
        self.dispatch(self.bus.get())

      time.sleep(0.25)
