myl = list(input())
size = len(myl)

for p in range(size):
    mymin = max(myl)
    for q in range(size-p):
        if myl[q] <= mymin:
            mymin = myl[q]

    myl[myl.index(mymin)] = myl[size-p-1]
    myl[size-p-1] = mymin

for i in range(size):
    print(myl[i], end='')