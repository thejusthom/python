class Solution:
    def lengthOfLongestSubstring1(self, s):
        sub_set = set()
        i,length,max_len = 0,0,0
        while i < len(s):
            if s[i] not in sub_set:
                sub_set.add(s[i])
                length += 1
            else:
                sub_set = set()
                sub_set.add(s[i])
                length = 1
            max_len = max(max_len,length)
            i += 1
        return max_len
    
    def lengthOfLongestSubstring(self,s):
        sub_set = set()
        l, length = 0,0
        for r in range(len(s)):
            while s[r] in sub_set:
                sub_set.remove(s[l])
                l += 1
            sub_set.add(s[r])
            length = max(length,r-l+1)
        return length
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s)) 
