"""
The main module
"""


class InvalidInputException(Exception):
	def __str__(self):
		return 'Invalid input.'

def add_numbers(numbers: str) -> int:
	"""
	Take upto two numbers in string format and return their sum in integer format 
	"""
	# Input can be an empty string too
	if numbers == '':
		return 0
	
	if len(numbers) >= 1:
		numbers = numbers.replace('\n',',')
		try:
			nums = list(map(int, numbers.split(',')))
			return sum(nums)
		except:
			raise InvalidInputException
