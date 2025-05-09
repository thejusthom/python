height = [1,8,6,2,5,4,8,3,7]
result = 0
l,r = 0, len(height) - 1
while l < r:
    area = min(height[l],height[r]) * (r-l)
    result = max(result,area)
    if height[l] > height[r]:
        r -= 1
    else:
        l += 1
print(result)
