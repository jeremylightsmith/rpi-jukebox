import time

datadir = "/mnt/bigdaddy"

from music import MusicPlayer
player = MusicPlayer(datadir + "/music")

from card_store import CardStore
store = CardStore(datadir)

def card_read(id):
  index = store.index_of(id)
  print "playing song ", index
  player.play_song(index)

def stop():
  player.stop_song()

def next_song():
  print "next_song"

def previous_song():
  print "previous_song"

def repeat():
  print "repeat"

def no_repeat():
  print "no_repeat"

def play():
  print "play"

def quit():
  exit(0)

handlers = {
  'card_read': card_read,
  'stop': stop,
  'next_song': next_song,
  'previous_song': previous_song,
  'repeat': repeat,
  'no_repeat': no_repeat,
  'play': play,
  'quit': quit,

  # 'first_song':first_song,
  # 'last_song':last_song,
  # 'volume_down':volume_down,
  # 'volume_up':volume_up,
  # 'home':home,
}

def dispatch(event):
  if event[0] in handlers:
    handlers[event[0]](*event[1:])

def start_dispatching(bus):
  while True:
    while not bus.empty():
      dispatch(bus.get())

    time.sleep(0.25)


