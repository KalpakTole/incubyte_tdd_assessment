"""
The main module
"""


class InvalidInputException(Exception):
	def __str__(self):
		return 'Invalid input.'


class NegativeNumberException(Exception):
	def __str__(self):
		return 'Negatives not allowed'


def add_numbers(numbers: str) -> int:
	"""
	Take upto two numbers in string format and return their sum in integer format
	"""
	# Input can be an empty string too
	if numbers == '':
		return 0

	if numbers[:2] == '//':
		delimiter = numbers[2]
		numbers = numbers[3:].replace('\n', '')
	else:
		delimiter = ','
		numbers = numbers.replace('\n', ',')
	nums = numbers.split(delimiter)
	if '' in nums:
		raise InvalidInputException
	else:
		negs = []
		for num in nums:
			if num[0] == '-':
				negs.append(num)
		if len(negs) >= 1:
			print('Negative inputs:',*negs)
			raise NegativeNumberException
	return sum(list(map(int, nums)))

