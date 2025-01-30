def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def russian(a,b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x%2 == 1:
            z = z+y
        x = x >> 1
        y = y << 1
    return z

def russian_rec(a,b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return 2 * russian_rec(a/2,b)
    return b + 2 * russian_rec((a-1)/2,b)

# print(naive(300000,2000000))
# print(russian(300000,2000000))
print(russian_rec(300000,2000000))


# print(14>>1)

