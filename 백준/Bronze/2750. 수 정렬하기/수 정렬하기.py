number = int(input())
myl = list()

for i in range(number):
    x = int(input())
    myl.append(x)

myl.sort()

for k in range(number):
    print(myl[k])

