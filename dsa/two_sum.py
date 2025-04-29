nums = [2,7,11,15]
target = 9
numMap = {}
for i in range(len(nums)):
    numMap[nums[i]] = i
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in numMap:
        print(i,numMap[diff])