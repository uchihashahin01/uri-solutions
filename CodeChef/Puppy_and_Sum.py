def my_func(a,b):
    for _ in range(a):
        b = (b *(b +1)) // 2
    print(b)


for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    
    my_func(a,b)
