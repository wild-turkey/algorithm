from os.path import split

money = int(input())
price = list(map(int, input().split(' ')))

xmoney = money
ymoney = money

xstocks = 0
ystocks = 0

last = price[0]

up = 0
down = 0

for p in price:

    if last > p:
        down += 1
        up = 0
    elif last < p:
        up += 1
        down = 0
    else:
        up =0
        down = 0


    if xmoney >= p:
        xstocks += xmoney // p
        xmoney -= (xmoney // p) * p

    if down >= 3:
        ystocks += ymoney // p
        ymoney -= (ymoney // p) * p

    if up >= 3:
        ymoney += ystocks * p
        ystocks = 0

    last = p

xfinal = price[13] * xstocks + xmoney
yfinal = price[13] * ystocks + ymoney


if xfinal > yfinal:
    print("BNP")
elif xfinal == yfinal:
    print("SAMESAME")
else: print("TIMING")