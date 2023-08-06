from mpmath import *


class mptaylor:

    def __init__(self, f=sin, p=0, d=5):
        mp.dps = 15
        mp.pretty = True

        self.poly = taylor(f, p, d)
        nprint(chop(self.poly))


    def predict(self, x):
        return polyval(self.pooly[::-1], x - p)
