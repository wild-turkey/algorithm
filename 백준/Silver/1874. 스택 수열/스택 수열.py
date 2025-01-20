num = int(input())
mylist = [0] * num
stack = []
result = []
okay=True
k = 1

for i in range(num):
    mylist[i] = int(input())

for i in range(num):
    su = mylist[i]
    if k <= su:
        while k <= su:
            stack.append(k)
            k+=1
            result.append('+')
        stack.pop()
        result.append('-')

    else:
        n = stack.pop()
        if su < n:
            print("NO")
            okay = False
            break
        else:
            result.append('-')
if okay:
    for i in result:
        print(i)



