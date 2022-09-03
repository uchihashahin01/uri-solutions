n,atm=map(float,input().split())
n=int(n)


if (n + 0.50 <= atm and n%5 == 0):
    result = (atm - n) - 0.50
    print(float(result))
else:
    print(float(atm))

