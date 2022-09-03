for _ in range(int(input())):
    c = sum(list(map(int,input().split())))
    if c < 3:
        print(1)
    elif c >= 3 and c <= 10:
        print(2)
    elif c >= 11 and c <= 60:
        print(3)
    else :
        print(4)