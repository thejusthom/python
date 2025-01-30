import sys

s, t = 'axc', 'ahxgdc'
S, T = len(s), len(t)
if s == "": 
    print(True)
    sys.exit() 
if S > T: 
    print(False)
    sys.exit() 
j = 0
for i in range(T):
    if t[i] == s[j]:
        if i == T-1:
            print(True)
            sys.exit() 
        else:
            j += 1
print(False)

