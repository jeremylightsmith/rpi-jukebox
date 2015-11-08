# Jeremy's Jukebox 2.0
# Author: Jeremy Lightsmith
# Copyright (c) 2015 Jeremy Lightsmith

import time
import binascii
import Adafruit_PN532 as PN532
import os.path
from datetime import datetime

# PN532 configuration for a Raspberry Pi:
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# Create and initialize an instance of the PN532 class.
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()

class CardReader:
    def __init__(self, datadir):
        self.card_list_file = os.path.join(datadir, "cards.txt")
        self.card_list = self.__load_card_list()

    # read the index (0,1,2,3,...) of a mifare card
    # if it doesn't have an index, assign one
    def read(self):
        time.sleep(0.5)

        uid = None
        while uid is None:
            uid = pn532.read_passive_target()
        uid = binascii.hexlify(uid)

        if not uid in self.card_list:
            self.card_list.append(uid)
            self.__write_card_list()
            print "card added"

        n = self.card_list.index(uid)

        if n == 0: 
            return ["stop"]
        
        else:
            return ["card", n - 0]

    def __load_card_list(self):
        if os.path.isfile(self.card_list_file):
            with open(self.card_list_file, "r") as f:
                return f.read().split("\n")
        else:
            return []

    def __write_card_list(self):
        with open(self.card_list_file, "w") as f:
            f.write("\n".join(self.card_list))

