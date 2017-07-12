# -*- coding: utf-8 -*-

from datetime import datetime


class Problem:
    def run(self):
        begin = datetime.now()
        print "answer of %s is: %s" % (self.name, self.solve())
        print "cost: %s to solve %s" % (datetime.now() - begin, self.name)
