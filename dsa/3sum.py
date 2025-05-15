nums = [-1,0,1,2,-1,-4]
answer = []
le = len(nums)
nums.sort()
for i in range(le):
    if nums[i] > 0:
        break
    elif i > 0 and nums[i-1] == nums[i]:
        continue
    l, r = i+1, le-1
    while l < r:
        sum  = nums[i] + nums[l] + nums[r]
        if sum > 0:
            r -= 1
        elif sum < 0:
            l += 1
        else:
            answer.append([nums[i],nums[l],nums[r]])
            l +=1
            while l < r and nums[l] == nums[l-1]:
                l += 1
print(answer)
