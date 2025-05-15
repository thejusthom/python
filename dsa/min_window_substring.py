class Solution:
    def minWindow(self,s,t):
        # slen = len(s)
        # tlen = len(t)
        if t == "":
            return ""
        tMap,window = {},{}
        for tt in t:
            tMap[tt] = 1 + tMap.get(tt,0)
        have, need = 0,len(tMap)
        l=0
        maxLen = float("infinity")
        pos = [-1,-1]
        for r in range(len(s)):
            st = s[r]
            window[st] = 1 + window.get(st,0)
            if st in tMap and window[st] == tMap[st]:
                have += 1
            while have == need:
                le = r - l + 1
                if le < maxLen:
                    maxLen = le
                    pos = [l,r]

                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        l, r = pos
        return s[l : r + 1] if maxLen != float("infinity") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s,t))