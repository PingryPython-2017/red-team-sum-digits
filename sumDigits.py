def sumDigits(number):
	""" Returns the sum of each digit in number """
	
	if number == 0: # Terminating case
		return 0

	return (number % 10) + sumDigits(number // 10) # Recursive call

