from collections import  deque

num = int(input())

myq = deque()

for i in range(1,num+1):
    myq.append(i)

while len(myq) > 1:
    myq.popleft()
    myq.append(myq.popleft())

print(myq[0])