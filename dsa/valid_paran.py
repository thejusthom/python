class Solution:
    def isValid(self,s):
        stack = []
        mapping = {"(":")","[":"]","{":"}"}
        for st in s:
            if st == "(" or st == "[" or st == "{":
                stack.append(st)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if st == ')' and top != '(':
                    return False
                if st == ']' and top != '[':
                    return False
                if st == '}' and top != '{':
                    return False
                stack.pop()
        return not stack


s = "[]"
print(Solution().isValid(s))