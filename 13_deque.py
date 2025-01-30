from collections import deque

d = deque()
d.append(1)
d.append(4)
d.append(6)
d.appendleft(7)
d.popleft()
d.pop()
print(d)