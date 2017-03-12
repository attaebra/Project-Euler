def largePalindrome():
	all = []
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			number = i*j
			reversed = str(number)[::-1]
			#print("The number %s | the reversed number %s." % (number, reversed))
			if (str(number) == reversed):
				all.append(number)
	return max(all)
value = largePalindrome()
print(value)