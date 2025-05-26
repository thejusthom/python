class Solution(object):
    def generateParenthesis(self, n):
        stack,res = [],[]
        def backtrack(open,close):
            if open == close == n:
                return res.append("".join(stack))
            if open < n:
                stack.append("(")
                backtrack(open+1,close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open,close+1)
                stack.pop()
        backtrack(0,0)
        return res
print(Solution().generateParenthesis(3))