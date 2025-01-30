import math

def time(n):
    """ Return the number of steps 
    necessary to calculate
    `print countdown(n)`"""
    steps = 0
    # YOUR CODE HERE
    steps = math.ceil(n/5.0)
    print(steps)
    return steps

def countdown(x):
    y = 0
    time(x)
    while x > 0:
        x = x - 5
        y = y + 1
    return y

print (countdown(10))