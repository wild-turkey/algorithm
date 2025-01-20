import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

node, edge = map(int, input().split(' '))

link = [[]for _ in range (node+1)]
visit = [False] * (node+1)


def DFS(n):
    visit[n] = True
    for k in link[n]:
        if not visit[k]:
            DFS(k)


for _ in range(edge):
    x, y = map(int, input().split(' '))
    link[x].append(y)
    link[y].append(x)

count = 0

for i in range(1,node+1):
    if not visit[i]:
        count += 1
        DFS(i)

print(count)