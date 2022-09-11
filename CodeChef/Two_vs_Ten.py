for _ in range(int(input())):
    a= int(input())

    if a % 10 == 0:
        print("0")
    elif (a*2) % 10 == 0:
        print("1")
    else:
        print("-1")