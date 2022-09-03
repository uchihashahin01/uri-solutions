T = int(input())
while (T > 0):
    a, b = map(int, input().split())

    if (a == 0):
        print("Liquid")
    elif (b == 0):
        print("Solid")
    else:
        print("Solution")

    T -= 1