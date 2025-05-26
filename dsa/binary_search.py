class Solution(object):
    def search(self, nums, target):
        l,r = 0,len(nums)-1
        for i in range(l-1,r,1):
            m = (l + r) // 2
            if nums[m] == target:
                return m                
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1
    
print(Solution().search([9],9))