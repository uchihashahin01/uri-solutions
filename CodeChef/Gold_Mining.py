def my_func(a,b,c):
    if ((a+1)*c) >= b:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    
    my_func(a,b,c)