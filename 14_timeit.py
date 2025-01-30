import random
import timeit
print('N\tSum Time')
for t in [2**_ for _ in range(1,9)]:
	numbers = [random.randint(1,9) for _ in range(t)]
	m = timeit.timeit(stmt='sum = 0\nfor d in numbers:\n\tsum',
					setup='import random\nnumbers = '+ str(numbers))
	print('{0:d}\t{1:f}'.format(t,m))





	