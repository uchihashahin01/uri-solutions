def my_func(a, b):
    # bites = a
    # for _ in range(bites):
    #     bites -= b
    
    # if bites == 0:
    #     print(int(a/b))
    # elif bites < 0:
    #     print("-1")

    if a % b == 0:
        print(int(a/b))
    else:
        print("-1")
for _ in range(int(input())):
    a,b = map(int,input().split())
    
    my_func(a,b)