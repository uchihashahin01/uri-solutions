def my_func(x,y,p,q):
    if x + 10*p > y + 10*q:
        print("Chefina")
    elif x + 10*p < y + 10*q:
        print("Chef")
    else:
        print("Draw")


for _ in range(int(input())):
    x,y,p,q = list(map(int,input().split()))
    
    my_func(x,y,p,q)