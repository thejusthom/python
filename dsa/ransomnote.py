from collections import defaultdict


ransomNote = "aab"
magazine = "aba"

d = defaultdict(int)

for mag in magazine:
    d[mag] += 1

for ran in ransomNote:
    if ran not in d:
        print('False')
    elif d[ran] == 1:
        del d[ran]
    else:
        d[ran] -= 1
print('True')