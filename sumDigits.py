def sumDigits(number):
	""" Returns the sum of each digit in number """
	
	word = str(number)
	digit = int(word[0])
	newNumber = int(word[1:])
	
	if len(word) == 0: # Base case
		return 0
	digit + sumDigits(newNumber)

print(sumDigits(999))