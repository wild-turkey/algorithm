n = int(input())
data = list(map(int, input().split(' ')))

m = int(input())
find = list(map(int, input().split(' ')))

data.sort()

for i in range(m):
    start = 0
    end = len(data) -1
    found = False

    while start <= end:
        midi = int((start + end)/2)
        midv = data[midi]

        if find[i] > midv:
            start = midi + 1
        elif find[i] < midv:
            end = midi - 1
        else:
            found = True
            break

    if found: print('1')
    else: print('0')