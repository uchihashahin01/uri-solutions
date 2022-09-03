def diff(a,b,c):

    if abs(a - b) <= c:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    
    diff(a,b,c)