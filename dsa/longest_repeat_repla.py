class Solution:
    def characterReplacement(self,s,k):
        freq = {}
        res,l = 0,0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l+=1
            res = max (res, r-l+1)
        return res

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s,k))    