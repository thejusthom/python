class Solution(object):
    def search(self, nums, target):
        l,r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        min_i = l

        if min_i == 0:
            l,r = 0,len(nums)-1
        elif target >= nums[0] and target <= nums[min_i-1]:
            l,r = 0,min_i-1
        else:
            l,r = min_i,len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1
nums = [3,1]
target = 3
print(Solution().search(nums,target))