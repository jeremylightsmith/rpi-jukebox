from Queue import Queue
from card_reader import CardReader
from remote_listener import RemoteListener
from keyboard_listener import KeyboardListener
from dispatcher import Dispatcher

print "Welcome to Jeremy's Jukebox 3.0"
print ''

q = Queue()

# CardReader(q).start()
# RemoteListener(q).start()
# Dispatcher("/mnt/bigdaddy").run(q)

KeyboardListener(q).start()
Dispatcher("/Users/jeremy/src/jukebox").run(q)
