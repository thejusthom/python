class Solution(object):
    def carFleet(self, target, position, speed):
        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >  1 and stack[-2] > stack[-1]:
                stack.pop()
        return len(stack)


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(Solution().carFleet(target,position,speed))