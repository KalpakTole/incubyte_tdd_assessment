"""
The main module
"""


def add_numbers(numbers: str) -> int:
	"""
	Take upto two numbers in string format and return their sum in integer format 
	"""
	# Input can be an empty string too
	if numbers == '':
		return 0
	
	if len(numbers) == 1:
		return int(numbers)