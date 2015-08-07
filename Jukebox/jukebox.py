# Jeremy's Jukebox 2.0
# Author: Jeremy Lightsmith
# Copyright (c) 2015 Jeremy Lightsmith

import time

# datadir = "/home/pi/music"
# from nfc import MifareReader
# reader = MifareReader(datadir)

datadir = "../music"
from keyboard import KeyboardReader
reader = KeyboardReader()

from music import MusicPlayer
player = MusicPlayer(datadir)

print "Welcome to Jeremy's Jukebox 2.0"
print ''


while True:
    card = reader.read()

    if card == 0:
        player.stop_song()
    else:
        player.play_song(card)

    time.sleep(0.5)

