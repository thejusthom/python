class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a+b))
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a-b))
            elif t == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a*b))
            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(t))
        return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens)) 