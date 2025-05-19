from collections import deque


class Solution:
    def max_sliding_window(self, nums, k):
        output = []
        q = deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r+1 >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().max_sliding_window( nums, k))