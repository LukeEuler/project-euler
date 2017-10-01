# -*- coding: utf-8 -*-

from datetime import datetime


class Problem:
    def __init__(self):
        self.name = "Default name"

    def run(self):
        begin = datetime.now()
        print "answer of %s is: %s" % (self.name, self.solve())
        print "cost: %s to solve %s" % (datetime.now() - begin, self.name)
