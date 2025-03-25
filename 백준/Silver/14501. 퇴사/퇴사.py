n = int(input())

time = [0] * (n+1)
pay = [0] * (n+1)
best = [0] * (n+2)

for i in range(1,n+1):
    time[i], pay[i] = map(int,input().split(' '))

for i in range(n,0,-1):
    if (i + time[i] -1) > n:
        best[i] = best[i+1]
    else:
        best[i] = max(best[i+1],best[i+time[i]]+pay[i])

print(best[1])