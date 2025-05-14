class Solution:
    def checkInclusion(self,s1,s2):
        len1,len2 = len(s1),len(s2)
        s1a,s2a = [0]*26,[0]*26
        if len1 > len2:
            return False
        for i in range(len1):
            s1a[ord(s1[i]) - 97] += 1
            s2a[ord(s2[i]) - 97] += 1
        if s1a == s2a:
            return True
        for i in range(len1, len2):
            s2a[ord(s2[i]) - 97] += 1
            s2a[ord(s2[i-len1]) - 97] -= 1
            if s1a == s2a:
                return True
        return False

s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1,s2))