def my_func(a,b):
    print(sum(a)+sum(b))

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    
    my_func(a,b)