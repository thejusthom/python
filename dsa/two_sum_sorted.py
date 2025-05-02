numbers = [2,7,11,15]
target = 9
l,r = 0, len(numbers) - 1
while l < r:
    sum = numbers[l] + numbers[r]
    if sum > target:
        r -= 1
    elif sum < target:
        l += 1
    else:
        print([l,r])
        l += 1
