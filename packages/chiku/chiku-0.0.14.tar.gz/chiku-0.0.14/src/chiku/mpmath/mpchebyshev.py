from mpmath import *


class mpchebyshev:

    def __init__(self, f=cos, r=[1,2], d=5):
        mp.dps = 15
        mp.pretty = True

        self.poly, self.err = chebyfit(f, r, d, error=True)

        nprint(self.poly)
        nprint(self.err, 12)


    def predict(self, x):
        return nprint(polyval(self.poly, x), 12)
