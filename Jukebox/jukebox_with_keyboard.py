# Jeremy's Jukebox 2.0
# Author: Jeremy Lightsmith
# Copyright (c) 2015 Jeremy Lightsmith

import time
import sys
from Queue import Queue
from threading import Thread

# datadir = "/home/pi/music"
datadir = "../music"

from music import MusicPlayer
player = MusicPlayer(datadir)

print "Welcome to Jeremy's Jukebox 2.0"
print ''


q = Queue()


from keyboard import KeyboardReader
keyboard_reader = KeyboardReader()
def read_keys():
    while True:
        q.put(keyboard_reader.read())

t = Thread(name="keys", target=read_keys)
t.daemon = True
t.start()


# from nfc import CardReader
# card_reader = CardReader(datadir)
# def read_cards():
#     while True:
#         q.put(card_reader.read())

# t = Thread(name="cards", target=read_cards)
# t.daemon = True
# t.start()


def up(event):
    print("up")

def right(event):
    print("right")

def down(event):
    print("down")

def left(event):
    print("left")

def enter(event):
    print("enter")

def quit(event):
    print("quit")
    sys.exit()

def card(event):
    player.play_song(event[1])

def stop(event):
    player.stop_song()

dispatch = {
    'up':up,
    'right':right,
    'down':down,
    'left':left,
    'enter':enter,
    'card':card,
    'stop':stop,
    'quit':quit}


while True:
    event = q.get()

    dispatch[event[0]](event)

    q.task_done()


