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

# def up(event):
#     print("up")

# def right(event):
#     print("right")

# def down(event):
#     print("down")

# def left(event):
#     print("left")

# def enter(event):
#     print("enter")

# def quit(event):
#     print("quit")
#     sys.exit()

def card_read(id):
  index = store.index_of(id)
  print "playing song ", index
  player.play_song(index)
  # print "got card: " + id

def next():
  print "got next"

# def card(event):
#     player.play_song(event[1])

# def stop(event):
#     player.stop_song()

dispatch = {
  'card_read': card_read,
  'next': next
}

q = Queue()

CardReader(q).start()
RemoteListener(q).start()

while True:
  while not q.empty():
    event = q.get()
    dispatch[event[0]](*event[1:])

  time.sleep(0.5)


