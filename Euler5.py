import time

checkList = [11, 13, 14, 16, 17, 18, 19, 20]
start = time.time()

def findSolution():
	for num in range(2520, 999999999, 2520):
		if all(num % n == 0 for n in checkList):
			return num
	return None

solution = findSolution()
end = time.time()
final = start - end
print("The solution is %d, in %d seconds." % (solution, final))