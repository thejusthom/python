# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [1,0,1,2]
# length = len(nums)
# print(length)
# low = min(nums)
# print(low)
# nums.sort()
setnum = set(nums)
longest = 0
print(setnum)
for n in setnum:
    if n-1 not in setnum:
        length = 1
        while n+1 in setnum:
            n += 1
            length += 1
        longest = max (length,longest)
print(longest)