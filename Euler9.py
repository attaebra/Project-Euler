import math

def pythagorean_triple():
	for a in range(1,1000):
		for b in range(a+1, 1000):
			c = b + 1
			
			while (c*c < (a*a + b*b)):
				c = c + 1
			if ((c*c == (a*a + b*b)) and (c <= 1000)):
				if ((a+b+c) == 1000):
					return a*b*c

solution = pythagorean_triple()
					
print(solution)