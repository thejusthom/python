import sys
strs = ["flower","flow","flight"]
min_len = 201
for st in strs:
    if len(st) < min_len:
        min_len = len(st)
i = 0
while i < min_len:
    for st in strs:
        if st[i] != strs[0][i]:
            print(st[:i])
            sys.exit() 
    i += 1        
print(st[:i])