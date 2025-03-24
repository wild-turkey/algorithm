n = int(input())
mylist = [0] * (n+1)
mylist[1] = 0

for i in range(2,n+1):
    mylist[i] = mylist[i-1] + 1
    if i % 3 == 0:
        mylist[i] = min(mylist[int(i/3)]+1 , mylist[i])
        
    if i % 2 == 0:
        mylist[i] = min(mylist[int(i / 2)] + 1, mylist[i])

print(mylist[n])
