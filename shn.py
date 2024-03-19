import math

populations = list([[0.25, 0.25, 0.25, 0.25],
					[0.50, 0.30, 0.20, 0.10],
					[0.50, 0.50, 0.0, 0.0],
					[1, 0, 0, 0]])

def shannon(dist):
	sum = 0
	for i in dist:
		if i > 0:
			sum -= i*math.log(i)
	return(sum)

for j in populations:
	s = shannon(j)
	print('shn = ', round(s, 3), 'exp =', round(math.exp(s), 3))	