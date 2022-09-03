def my_func(a,b):
    if sum(a) > sum(b):
        print("1")
    else:
        print("2")
        
for _ in range(int(input())):
    c,d,e,f,g,h = list(map(int,input().split()))
    
    a = [c,d,e]
    b = [f,g,h]
    
    my_func(a,b)