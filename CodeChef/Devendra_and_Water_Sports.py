def my_func(a,b,c,d,e):
    remaining = (a - b) 
    need_to_spend = (c+d+e)
    if need_to_spend <= remaining:
        print("YES")
    else:
        print("NO")
    
    
for _ in range(int(input())):
    a,b,c,d,e = list(map(int,input().split()))

    my_func(a,b,c,d,e)
    
    