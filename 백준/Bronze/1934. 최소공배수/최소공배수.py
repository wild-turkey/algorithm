n = int(input())

for _ in range(n):
    x, y = map(int, input().split(' '))
    a, b = x, y
    while b != 0:
        a, b = b, a % b

    print(int(x*y//a))