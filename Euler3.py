def primeFactorization(n):
	factors = []
	d = 2
	while d*d <= n:
		if n % d == 0:
			n //= d
			factors.append(d)
		else:
			d += 1
	if n > 1:
		factors.append(n)
	return factors
	
primeFactors = primeFactorization(600851475143)
print(primeFactors[-1])
