prices = [7,1,5,3,6,4]
# max_prof = 0
# min_val = float('inf')
# O(N square)
# P = len(prices)
# for i in range(P-1):
#     for j in range(i,P,1):
#         if prices[j] - prices[i] > diff:
#             diff = prices[j] - prices[i]
max_prof = 0
min_val = float('inf')
for price in prices:
    if price < min_val:
        min_val = price
    if price - min_val > max_prof:
        max_prof = price - min_val
print(max_prof)