def my_func(a,b,c,d,e):
    if a*b >= 42:
        print(e)
    elif a*b >=21:
        print(d)
    elif a*b >= 10:
        print(c)
    else:
        print(0)
    


for _ in range(int(input())):
    a,b,c,d,e = list(map(int,input().split()))

    my_func(a,b,c,d,e)