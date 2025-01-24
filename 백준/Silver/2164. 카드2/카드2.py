from  collections import deque
n = int(input())
myd = deque()

for i in range(1,n+1):
    myd.append(i)

for i in range(n-1):
    myd.popleft()
    myd.append(myd.popleft())

print(myd[0])