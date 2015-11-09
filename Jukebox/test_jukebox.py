from Queue import Queue
from keyboard_listener import KeyboardListener
from dispatcher import Dispatcher

print "Welcome to Jeremy's Test Jukebox 3.0"
print ''

q = Queue()

KeyboardListener(q).start()
Dispatcher(q, "/Users/jeremy/src/jukebox").start()
