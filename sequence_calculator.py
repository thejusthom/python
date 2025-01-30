# (1)
# Complete the sequence_calculator function, which should
# Return the n-th number of the sequence S_n, defined as:
# S_n = 3*S_(n-1) - S_(n-2), with S_0 = 0 and S_1 = 1.
# Your implementation should minimize the execution time.
#
# (2)
# Find the time complexity of the proposed solution, using
# the "Big O" notation, and explain in detail why such
# complexity is obtained, for n ranging from 0 to at least
# 100000. HINT: you are dealing with very large numbers!
#
# (3)
# Plot the execution time VS n (again, for n ranging from 0
# to at least 100000).
#
# (4)
# Confirm that the empirically obtained time complexity curve
# from (3) matches the claimed time complexity from (2) (e.g.
# by using curve fitting techniques).


# def sequence_calculator(n):
#     return None


# print(sequence_calculator(100000))

import time
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.set_int_max_str_digits(100000)

# def sequence_calculator(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     prev1, prev2 = 1, 0
#     for _ in range(2, n + 1):
#         current = 3 * prev1 - prev2
#         prev2 = prev1
#         prev1 = current

#     return prev1

def sequence_calculator(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    def matrix_multiply(a, b):
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]
    
    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        if power % 2 == 0:
            half = matrix_power(matrix, power // 2)
            return matrix_multiply(half, half)
        return matrix_multiply(matrix, matrix_power(matrix, power - 1))
    
    base_matrix = [[3, -1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n-1)
    return result_matrix[0][0]

# Testing the function for a large value
print(sequence_calculator(100000))

# Measuring execution time for varying n
times = []
values = range(0, 100001, 1000)

for n in values:
    start_time = time.time()
    sequence_calculator(n)
    end_time = time.time()
    times.append(end_time - start_time)

# Plotting the execution time vs. n
plt.figure(figsize=(10, 6))
plt.plot(values, times, label='Execution time')
plt.xlabel('n')
plt.ylabel('Execution time (seconds)')
plt.title('Execution Time vs. n for sequence_calculator')
plt.legend()
plt.show()

# Curve fitting to confirm O(n) time complexity
coefficients = np.polyfit(values, times, 1)
print(f"Estimated time complexity fit (linear): {coefficients[0]} * n + {coefficients[1]}")