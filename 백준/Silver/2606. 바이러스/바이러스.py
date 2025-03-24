n = int(input())
pair = int(input())
graph = {}
visited = [False] * (n + 1)
count = 0

def DFS(node):
    visited[node] = True
    for k in graph[node]:
        if visited[k] == False:
            visited[k] = True
            DFS(k)

for i in range(n):
    graph[i+1] = []

for _ in range(pair):
    x, y = map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

DFS(1)

for i in range(n+1):
    if visited[i] == True:
        count += 1

print(count-1)