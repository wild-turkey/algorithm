n, money = map(int, input().split(' '))

coin = [0]*n

for i in range(n):
    coin[i] = int(input())

count = 0

for i in range(n):
    available = money // coin[n-1-i]
    money = money % coin[n-1-i]
    count += available

print(count)