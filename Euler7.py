def generatePrimes():
	D = {}
	q = 2
	while True:
		if q not in D:
			yield q
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1

count = 0
value = 0
for p in generatePrimes():
	count += 1
	if count == 10001:
		value = p
		break

print("The value is: %d" % value)
		