n = int(input())
mylist = []
mylist = list(map(int,input().split(' ')))
length = [1] * n
big = 0
small = 0

for p in range(n):
    for q in range(p):
        if mylist[p] > mylist[q]:
            length[p] = max(length[p],length[q] + 1)

print(max(length))