import unittest
from chiku import mpmath

class Test_MPMath(unittest.TestCase):
	def test_mpmath(self):
		one = mpf(1)

		def f(x):
			return sqrt((one + 2*x)/(one + x))

		self.t = mpmath.mptaylor(f, 0, 6)
		self.p = mpmath.pade(self.t, 3, 3)
		self.x = 10

		self.assertAlmostEqual(self.p.predict(self.x), f(self.x), 2)

if __name__ == '__main__':
	unittest.main()
