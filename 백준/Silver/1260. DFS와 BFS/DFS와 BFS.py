from collections import deque
node, edge, start = map(int,input().split(' '))

link = [[] for _ in range(node+1)]

for _ in range(edge):
    x, y = map(int, input().split(' '))
    link[x].append(y)
    link[y].append(x)

for i in range(node+1):
    link[i].sort()

def DFS(n):
    visit[n] = True
    print(n, end=' ')
    for i in link[n]:
        if not visit[i]:
            DFS(i)

visit = [False] * (node+1)
DFS(start)

def BFS(n):
    q = deque()
    q.append(n)
    visit[n] = True

    while q:
        poped = q.popleft()
        print(poped, end=' ')
        for i in link[poped]:
            if not visit[i]:
                visit[i] = True
                q.append(i)

print()
visit = [False] * (node + 1)
BFS(start)
