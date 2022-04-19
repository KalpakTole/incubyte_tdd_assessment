"""
Test module for add_numbers.py
"""


import unittest2
from add_numbers import add_numbers


class TestAddNumbers(unittest2.TestCase):
	"""
	Test the function add_numbers from module add_numbers.py
	"""

	def test_empty_string(self):
		self.assertEqual(add_numbers(''), 0)

	def test_single_integer(self):
		self.assertEqual(add_numbers('1'), 1)
		self.assertEqual(add_numbers('2'), 2)


if __name__ == '__main__':
	unittest2.main()
