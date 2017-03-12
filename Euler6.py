def sumOfSquares(n):
	total = 0
	list = [i for i in range(1,n+1)]
	for i in list:
		total = total + i
	total = total**2
	
	return total
	
def squareOfSum(n):
	total = 0
	list = [i for i in range(1,100)]
	for i in list:
		total = total + i**2
	return total

value = sumOfSquares(100) - squareOfSum(100)
print("The answer is %d" % value)