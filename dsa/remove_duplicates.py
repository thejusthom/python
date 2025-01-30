nums = [0,0,1,1,1,2,2,3,3,4]
i,j = 0,1,1
len_nums = len(nums)
while i < len_nums:
    if nums[i] == nums[i-1]:
        i += 1
    else:
        nums[j] = nums[i]
        i += 1
        j += 1
print(j)
        