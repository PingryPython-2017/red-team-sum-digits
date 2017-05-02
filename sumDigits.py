def sumDigits(number):
	""" Returns the sum of each digit in number """
	if number == 0: # Base case
		return 0
	else:
		return (number % 10) + sumDigits(number // 10)

print(sumDigits(999))