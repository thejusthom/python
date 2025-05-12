prices = [1,2,4,2,5,7,2,4,9,0,9]
max_profit = 0
l,r = 0,1
size = len(prices)
while r < size:
    if prices[l] < prices[r]:
        max_profit = max(prices[r] - prices[l], max_profit)
    else:
        l = r
    r += 1
print(max_profit)
    