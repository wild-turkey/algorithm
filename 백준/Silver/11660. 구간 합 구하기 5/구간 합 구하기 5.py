import sys
input = sys.stdin.readline

size, n = map(int,input().split())

mainlist = [[0] * (size+1)]
grid = [[0]*(size+1) for i in range (size + 1)]

for i in range(size):
    templist = [0] + list(map(int, input().split()))
    mainlist.append(templist)

for p in range(1,size+1):
    for q in range(1, size + 1):
        grid[p][q] = grid[p-1][q] + grid[p][q-1] + mainlist[p][q] - grid[p-1][q-1]

for _ in range(n):
    x, y, a, b = map(int,input().split())
    print(grid[a][b] - grid[x-1][b] - grid[a][y-1] + grid[x-1][y-1])
