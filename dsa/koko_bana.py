class Solution(object):
    def minEatingSpeed(self, piles, h):
        l,r = 1,max(piles)
        res = r
        while l <= r:
            rate = (l+r)//2
            time = 0
            for p in piles:
                time += (p + rate - 1) // rate
            if  h < time:
                l = rate + 1
            else:
                r = rate - 1
                res = min(res,rate)
        return res


piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles,h))