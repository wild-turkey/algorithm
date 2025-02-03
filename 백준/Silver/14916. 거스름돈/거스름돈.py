n = int(input())
count = 0
possible = True

while(n %5 != 0):
    n -= 2
    count += 1
    if n<0:
        possible = False
        break

temp = n // 5
count += temp

if possible: print(count)
else: print("-1")
