s = 'III'
total_val = 0
roman_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# for s in s:
#     total_val = total_val + roman_val[s]
# print(total_val)
print(len(s))
for i in range(len(s)):
    if i<len(s)-1 and roman_val[s[i]] < roman_val[s[i+1]]:
        total_val = total_val - roman_val[s[i]]
    else:
        total_val = total_val + roman_val[s[i]]
print(total_val)