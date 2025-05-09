#left - after non 0 - 
# decrease - note down peak, add level by diff, decrease again
# increase 
height = [0,2,0,3,1,0,1,3,2,1]
l = len(height)
maxL,maxR = [0]*l,[0]*l
max = 0
for i in range(l):
    if height[i] > max:
        max = height[i]
    maxL[i] = max
max = 0
for i in range(l-1,-1,-1):
    if height[i] > max:
        max = height[i]
    maxR[i] = max
print(maxL)
print(maxR)
totalWater = 0
for i in range(l):
    if min(maxL[i],maxR[i]) - height[i] > 0:
        totalWater = totalWater + min(maxL[i],maxR[i]) - height[i]
print(totalWater)