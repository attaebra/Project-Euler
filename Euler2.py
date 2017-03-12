def getFibonnaci():
	yield 0
	a, b = 0, 1
	
	while True:
		yield b
		print("The value is: %d" % b)
		b = a + b
		a = b - a
		
values = []
for num in getFibonnaci():
	if num > 4000000:
		break
	values.append(num)

sum = 0
for value in values:
	if (value%2 == 0):
		sum += value
		
print(sum)