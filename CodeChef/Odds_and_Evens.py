def my_func(a,b):
    if (a+b) % 2 == 0:
        print("Bob")
    else:
        print("Alice")
        
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    
    my_func(a,b)