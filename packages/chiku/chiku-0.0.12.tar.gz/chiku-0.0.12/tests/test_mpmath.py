import unittest
from chiku.mpmath import mptaylor,mppade


class Test_MPMath(unittest.TestCase):
	def test_mpmath(self):
		one = mptaylor.get_d(1)

		def f(x):
			return sqrt((one + 2*x)/(one + x))

		self.t = mptaylor(f, 0, 6)
		self.p = mppade(self.t, 3, 3)
		self.x = 10

		self.assertAlmostEqual(self.p.predict(self.x), f(self.x), 2)

if __name__ == '__main__':
	unittest.main()
