for _ in range(int(input())):
    a,b,c,d = list(map(int,input().split()))
    
    if a/b > c/d:
        print("Alice")
    elif a/b < c/d:
        print("Bob")
    else:
        print("Equal")