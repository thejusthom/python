from collections import defaultdict


text = "nlaebolko"
balloon = "balloon"
balloonMap = defaultdict(int)
for t in text:
    if t in balloon:
        balloonMap[t] += 1

if any(c not in balloonMap for c in balloon):
    print(0)
else:
    print(min(balloonMap['b'],balloonMap['a'],balloonMap['l']//2,balloonMap['o']//2,balloonMap['n']))
