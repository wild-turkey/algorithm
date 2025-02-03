import math

n = int(input())
arr = list(map(int, input().split()))
result = []

gcd = math.gcd(arr[0], arr[1])
for i in range(2, n):
    gcd = math.gcd(gcd, arr[i])

for k in range(1,int(math.sqrt(gcd))+1):
    if gcd % k == 0:
        result.append(k)
        if k != gcd // k:
            result.append(gcd//k)

result.sort()

for fin in result:
    print(fin)

'''
while(count <= min(arr)):
    for i in arr:
        if i % count != 0:
            possible = False
            break
        else: possible = True

    if possible:
        print(count)

    count += 1
'''