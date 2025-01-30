word1 = 'abc'
word2 = 'pqr'
A, B, a, b = len(word1), len(word2), 0, 0 
word = 1
merged = []
while a < (A if B > A else B):
    merged.append(word1[a])
    merged.append(word2[a])
    a += 1
while a < A:
    merged.append(word1[a])
    a += 1
while a < B:
    merged.append(word2[b])
    a += 1
print(''.join(merged))  