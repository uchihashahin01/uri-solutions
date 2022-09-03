def my_func(a,b,c):
    if (c * 2 + a >= b):
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))

    my_func(a,b,c)