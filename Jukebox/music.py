# Jeremy's Jukebox 2.0
# Author: Jeremy Lightsmith
# Copyright (c) 2015 Jeremy Lightsmith

import os
import glob
import os.path
import subprocess
import random
from datetime import datetime

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"

def non_hidden_file(s):
    return not os.path.basename(s).startswith(".")

class MusicPlayer:
    def __init__(self, datadir):
        self.datadir = datadir
        self.last_card = -1
        self.last_request = 0

    def __lookup_mpg123_pid(self):
        pid = subprocess.check_output("ps ax | grep mpg123 | grep -v grep | awk '{print $1;}'", shell=True).strip()
        if pid != '':
            return pid
        else:
            return None

    def __is_playing(self):
        return self.__lookup_mpg123_pid() != None

    def __lookup_songs(self, card):
        file = glob.glob(os.path.join(self.datadir, "{0}-*".format(card)))
        if file == []:
            return []
        elif os.path.isfile(file[0]):
            return [file[0]]
        else:
            files = glob.glob(os.path.join(file[0], "*"))
            return filter(non_hidden_file, files)

    def play_song(self, card):
        if self.__is_playing():
            time_since_last_request = (datetime.now() - self.last_request).total_seconds()
            print "time since last request:", time_since_last_request

            if card == self.last_card and time_since_last_request < 1:
                self.last_request = datetime.now()
                return

            self.stop_song()

        self.last_card = card
        songs = self.__lookup_songs(card)
        print "playing : ", songs
        self.last_request = datetime.now()
        if songs:
            random.shuffle(songs)
            playlist = " ".join(map(shellquote, songs))
            cmd = "mpg123 -q %s &" % playlist
            print(cmd)
            os.system(cmd)

    def stop_song(self):
        pid = self.__lookup_mpg123_pid()
        if pid != None:
            print "stopping song (pid: ", pid, ")"
            os.system("kill %s" % pid)
