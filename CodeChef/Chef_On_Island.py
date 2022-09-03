def my_func(a,b,c,d,e):
    if (min((a/c),b/d)>=e):
        print("YES")
    else:
        print("NO")
        
for _ in range(int(input())):
    a,b,c,d,e = list(map(int,input().split()))
    
    my_func(a,b,c,d,e)