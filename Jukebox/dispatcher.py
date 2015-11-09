import time
from music import MusicPlayer
from card_store import CardStore

class Dispatcher:
  def __init__(self, datadir):
    self.player = MusicPlayer(datadir + "/music")
    self.store = CardStore(datadir)

  def card_read(self, id):
    index = self.store.index_of(id)
    print "playing song ", index
    self.player.play_song(index)
  
  def stop(self):
    self.player.stop_song()
  
  def next_song(self):
    print "next_song"
  
  def previous_song(self):
    print "previous_song"
  
  def repeat(self):
    print "repeat"
  
  def no_repeat(self):
    print "no_repeat"
  
  def play(self):
    print "play"
  
  def quit(self):
    exit(0)

  def dispatch(self, event):
    handler = getattr(self, event[0], None)
    if handler is None:
      print "Couldn't find handler for ", event[0]
    else:
      handler(*event[1:])

  def run(self, bus):
    while True:
      while not bus.empty():
        self.dispatch(bus.get())

      time.sleep(0.25)


