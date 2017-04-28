def sumDigits(number):
	""" Returns the sum of each digit in number """
	if number == 0: # Base case
		return 0
	
	word = str(number)
	digit = int(word[0])
	newNumber = int(word[1:])
	
	digit + sumDigits(newNumber)

print(sumDigits(999))