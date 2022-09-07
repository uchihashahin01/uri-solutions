for i in range(int(input())):
    a,b = list(map(int,input().split()))
    
    if a < b:
        print("REPAIR")
    elif a == b:
        print("ANY")
    else:
        print("NEW PHONE")
        