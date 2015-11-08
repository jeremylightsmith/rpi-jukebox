import time
import os.path
from datetime import datetime

class CardStore:
    def __init__(self, datadir):
        self.card_list_file = os.path.join(datadir, "cards.txt")
        self.card_list = self.__load_card_list()

    # if it doesn't have an index, assign one
    def index_of(uid):
        if not uid in self.card_list:
            self.card_list.append(uid)
            self.__write_card_list()
            print "card added"

        return self.card_list.index(uid)

    def __load_card_list(self):
        if os.path.isfile(self.card_list_file):
            with open(self.card_list_file, "r") as f:
                return f.read().split("\n")
        else:
            return []

    def __write_card_list(self):
        with open(self.card_list_file, "w") as f:
            f.write("\n".join(self.card_list))

