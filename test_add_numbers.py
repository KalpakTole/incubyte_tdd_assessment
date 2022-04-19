"""
Test module for add_numbers.py
"""


import unittest2
from add_numbers import InvalidInputException, NegativeNumberException, add_numbers


class TestAddNumbers(unittest2.TestCase):
	"""
	Test the function add_numbers from module add_numbers.py
	"""

	def test_empty_string(self):
		self.assertEqual(add_numbers(''), 0)

	def test_single_integer(self):
		self.assertEqual(add_numbers('1'), 1)
		self.assertEqual(add_numbers('2'), 2)
	
	def test_multiple_comma_separted_integers(self):
		self.assertEqual(add_numbers('1,2,3'), 6)
		self.assertEqual(add_numbers('10,20,30,40'), 100)
	
	def test_valid_newline_separator(self):
		self.assertEqual(add_numbers('1\n2,3'), 6)
		
	def test_invalid_separators(self):	
		with self.assertRaises(InvalidInputException):
			add_numbers('1,\n\n,,')

	def test_different_delimiter(self):
		self.assertEqual(add_numbers('//;\n1;2'), 3)
		self.assertEqual(add_numbers('//:\n10:20:55'), 85)
	
	def test_negative_numbers(self):
		with self.assertRaises(NegativeNumberException):
			add_numbers('1,-2')
		with self.assertRaises(NegativeNumberException):
			add_numbers('1\n-2,3')
		with self.assertRaises(NegativeNumberException):
			add_numbers('//;\n1;-2')

if __name__ == '__main__':
	unittest2.main()
