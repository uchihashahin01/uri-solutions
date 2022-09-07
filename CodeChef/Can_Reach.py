for i in range(int(input())):
    a,b,c = list(map(int,input().split()))
    if a%c == 0 and b%c == 0:
        print("YES")
    else:
        print("NO")