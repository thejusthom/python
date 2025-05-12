class Solution:
    def lengthOfLongestSubstring(self, s):
        sub_set = set()
        i,length,max_len = 0,0,0
        while i < len(s):
            if s[i] not in sub_set:
                sub_set.add(s[i])
                length += 1
            else:
                sub_set = set()
                max_len = max(max_len,length)
                sub_set.add(s[i])
                length = 1
            i += 1
        return max_len
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s)) 
