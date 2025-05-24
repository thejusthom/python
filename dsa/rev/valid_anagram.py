class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dictS,dictT = {},{}
        for i in range(len(s)):
            dictS[s[i]] = 1+dictS.get(s[i],0)
            dictT[t[i]] = 1+dictT.get(t[i],0)
        return dictS == dictT

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s,t))