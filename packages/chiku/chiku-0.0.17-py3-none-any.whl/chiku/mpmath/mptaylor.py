from mpmath import *


class mptaylor:

    def __init__(self, f=sin, p=0, d=5):
        mp.dps = 15
        mp.pretty = True

        self.poly = taylor(f, p, d)
        self.len = len(self.poly)
        nprint(chop(self.poly))


    def predict(self, x):
        return polyval(self.poly[::-1], x - p)
