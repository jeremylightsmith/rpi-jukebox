from Queue import Queue
from card_reader import CardReader
from remote_listener import RemoteListener
from dispatcher import Dispatcher

print "Welcome to Jeremy's Jukebox 3.0"
print ''

q = Queue()

CardReader(q).start()
RemoteListener(q).start()
Dispatcher(q, "/mnt/bigdaddy").start()
