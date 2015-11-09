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
  def __init__(self, path, bus):
    super(SongPlayer, self).__init__()
    self.path = path
    self.bus = bus
    self.setDaemon(True)

  def run(self):
    cmd = "mpg123 -q %s" % shellquote(self.path)
    print(cmd)
    os.system(cmd)
    self.bus.put(["finished_song"])

class MusicPlayer:
  def __init__(self, datadir, bus):
    self.datadir = datadir
    self.bus = bus
    self.songs = []
    self.track = 0
    self.ignore_next_finished_song_event = False
    self.play_sound("i_am_listening")
    self.repeating = False

  def __lookup_mpg123_pid(self):
    pid = subprocess.check_output("ps ax | grep mpg123 | grep -v grep | awk '{print $1;}'", shell=True).strip()
    if pid != '':
      return pid
    else:
      return None

  def __is_playing(self):
    return self.__lookup_mpg123_pid() != None

  def __lookup_songs(self, card):
    file = glob.glob(os.path.join(self.datadir, "music/{0}-*".format(card)))
    if file == []:
      return []
    elif os.path.isfile(file[0]):
      return [file[0]]
    else:
      files = glob.glob(os.path.join(file[0], "*"))
      return filter(non_hidden_file, files)

  def __play(self):
    self.stop_song()
    self.player = SongPlayer(self.songs[self.track], self.bus)
    self.player.start()

  def next_song(self):
    if self.track + 1 < len(self.songs):
      self.track += 1
      self.__play()
    elif len(self.songs) > 0 and self.repeating:
      self.track = 0
      self.__play()

  def finished_song(self):
    if self.ignore_next_finished_song_event:
      self.ignore_next_finished_song_event = False
    else:
      self.next_song()

  def previous_song(self):
    if self.track > 0:
      self.track -= 1
    if len(self.songs) > 0:
      self.__play()

  def first_song(self):
    if len(self.songs) > 0:
      self.track = 0
      self.__play()

  def last_song(self):
    if len(self.songs) > 0:
      self.track = len(self.songs) - 1
      self.__play()

  def set_repeating(self, value):
    self.repeating = value
    if value:
      self.play_sound("repeating_on")
    else:
      self.play_sound("repeating_off")

  def play_song(self, card):
    self.songs = self.__lookup_songs(card)
    self.track = 0
    if self.songs:
      self.__play()

  def play_sound(self, name):
    path = os.path.join(self.datadir, "sounds/{0}.mp3".format(name))
    cmd = "mpg123 -q %s" % shellquote(path)
    print(cmd)
    subprocess.call(cmd, shell=True)

  def stop_song(self):
    pids = self.__lookup_mpg123_pid()
    if pids != None:
      for pid in pids.split("\n"):
        print "stopping song (pid: ", pid, ")"
        self.ignore_next_finished_song_event = True
        subprocess.Popen("kill %s" % pid, shell=True).wait()
