for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    
    if ((a+b)/2) > c:
        print("YES")
    else:
        print("NO")