def planebus(a,b):
    return (a+b)

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))

    if planebus(a,b) > c:
        print("TRAIN")
    elif planebus(a,b) >= c:
        print("EQUAL")
    else:
        print("PLANEBUS")