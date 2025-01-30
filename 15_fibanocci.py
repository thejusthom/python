def fib(n):
	a = b = 1
	series = [a,b]
	while n > 2:
		a,b = b, a+b
		series.append(b)
		n = n-1
	return series

print(fib(5))