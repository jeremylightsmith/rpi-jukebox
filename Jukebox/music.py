# Jeremy's Jukebox 2.0
# Author: Jeremy Lightsmith
# Copyright (c) 2015 Jeremy Lightsmith

import os
import os.path
import subprocess

class MusicPlayer:
    def __init__(self, datadir):
        self.datadir = datadir
        self.last_card = -1
        self.last_card_played_at = 0

    def __lookup_mpg123_pid(self):
        pid = subprocess.check_output("ps a | grep mpg123 | grep -v grep | awk '{print $1;}'", shell=True).strip()
        if pid != '':
            return pid
        else:
            return None

    def __is_playing(self):
        return self.__lookup_mpg123_pid() != None

    def __lookup_songs(self, card):
        songs = []
        for root, dirs, files in os.walk(os.path.join(self.datadir, "%i" % card)):
            for name in files:
                if not name.startswith("."):
                    songs.append(os.path.join(root, name))
        return songs

    def play_song(self, card):
        if self.__is_playing():
            if self.last_card != card and False:
                self.stop_song()
            else:
                self.stop_song()
                self.play_song(card)
        else:
            self.last_card = card
            songs = self.__lookup_songs(card)
            if songs:
                print "playing song ", card, " : ", songs
                os.system("mpg123 -q '%s' &" % songs[0])

    def stop_song(self):
        pid = self.__lookup_mpg123_pid()
        if pid != None:
            print "stopping song (pid: ", pid, ")"
            os.system("kill %s" % pid)



