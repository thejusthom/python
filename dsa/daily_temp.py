class Solution(object):
    def dailyTemperatures(self, temperatures):
        opstack,stack = [0]*len(temperatures),[]
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                opstack[stackI] = i - stackI
            stack.append([t,i])
        return opstack

print(Solution().dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73]))