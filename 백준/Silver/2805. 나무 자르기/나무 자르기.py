n, m = map(int,input().split(' '))
tree = list(map(int,input().split(' ')))

tree.sort()

small = 0
big = max(tree)
answer = 0

while small <= big:
    find = (small + big) // 2

    cut = 0
    start = 0
    for i in range(n):
        if tree[i] > find:
            start = i
            break

    cut = sum(tree[start:]) - find * (n - start)

    if cut >= m:
        answer = find
        small = find + 1
    else:
        big = find - 1

print(answer)