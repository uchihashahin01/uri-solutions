from math import floor


def calculation(a,b,c):
    return a * (b + floor(c/2))


for _ in range(int(input())):
    a,b,c,d = list(map(int,input().split()))

    if calculation(a,b,c) > d:
        print("NO")
    else:
        print("YES")