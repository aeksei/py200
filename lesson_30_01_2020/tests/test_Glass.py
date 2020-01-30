import unittest
from lesson_30_01_2020.py200_1_1 import Glass


class MyTestCase(unittest.TestCase):
	def test_init(self):
		self.assertRaises(TypeError, Glass, "st", 10)


if __name__ == '__main__':
	unittest.main()
