def my_func(a,b,c,d):
    if c/a > d/b:
        print("1")
    elif c/a < d/b:
        print("-1")
    else:
        print("0")
for _ in range(int(input())):
    a,b,c,d = list(map(int,input().split()))
    
    my_func(a,b,c,d)