def my_func(a,b,c,d):
    if a == c or b == d:
        print("YES")
    else:
        print("NO")
    
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    my_func(a,b,c,d)