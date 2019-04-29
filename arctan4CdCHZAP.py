import	math
from math import e
from math import atan

for B in range(1,1000000000):
	Y = B/100000000
	X = 16/6-(atan(225.75 * Y)-atan(-100.25 * Y))/(atan(1271.5 * Y)-atan(683 * Y))
	if abs(X) < 0.00001:
		print(Y)
		#break
