# Jeremy's Jukebox 3.0
# Author: Jeremy Lightsmith
# Copyright (c) 2015 Jeremy Lightsmith

import time
import sys
from Queue import Queue

datadir = "/mnt/bigdaddy"
# datadir = "../music"

from music import MusicPlayer
player = MusicPlayer(datadir + "/music")

print "Welcome to Jeremy's Jukebox 3.0"
print ''

# from nfc import CardReader
# reader = CardReader(datadir)

# from keyboard import KeyboardReader
# reader = KeyboardReader()

from card_reader import CardReader
from remote_listener import RemoteListener
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

dispatch = {
  'card_read': card_read,
  'stop': stop,
  'next_song': next_song,
  'previous_song': previous_song,
  'repeat': repeat,
  'no_repeat': no_repeat,
  'play': play,

  # 'first_song':first_song,
  # 'last_song':last_song,
  # 'volume_down':volume_down,
  # 'volume_up':volume_up,
  # 'home':home,

}

q = Queue()

CardReader(q).start()
RemoteListener(q).start()

while True:
  while not q.empty():
    event = q.get()
    if event[0] in dispatch:
      dispatch[event[0]](*event[1:])

  time.sleep(0.25)


