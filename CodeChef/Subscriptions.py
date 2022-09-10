from math import ceil


for _ in range(int(input())):
    a , b = list(map(int,input().split()))
    
    if a <= 6:
        print(b)
    else:
        print(ceil(a/6)*b)