import os
import glob
import os.path
import subprocess
import threading

def shellquote(s):
  return "'" + s.replace("'", "'\\''") + "'"

def non_hidden_file(s):
  return not os.path.basename(s).startswith(".")

class SongPlayer(threading.Thread):
  def __init__(self, path):
    super(SongPlayer, self).__init__()
    self.path = path
    self.setDaemon(True)

  def run(self):
    cmd = "mpg123 -q %s" % shellquote(self.path)
    print(cmd)
    os.system(cmd)
    print "done playing!"

class MusicPlayer:
  def __init__(self, datadir):
    self.datadir = datadir
    self.last_card = -1
    self.songs = []
    self.track = 0

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

  def next_song(self):
    if self.track + 1 < len(self.songs):
      self.track += 1
      self.stop_song()
      self.player = SongPlayer(self.songs[self.track])
      self.player.start()

  def previous_song(self):
    if self.track > 0:
      self.track -= 1
      self.stop_song()
      self.player = SongPlayer(self.songs[self.track])
      self.player.start()

  def play_song(self, card):
    if self.__is_playing():
      self.stop_song()

    self.last_card = card
    self.songs = self.__lookup_songs(card)
    self.track = 0
    # print "playing : ", self.songs
    if self.songs:
      # random.shuffle(songs)
      # playlist = " ".join(map(shellquote, songs))
      self.player = SongPlayer(self.songs[self.track])
      self.player.start()

  def stop_song(self):
    pid = self.__lookup_mpg123_pid()
    if pid != None:
      print "stopping song (pid: ", pid, ")"
      subprocess.Popen("kill %s" % pid, shell=True).wait()
