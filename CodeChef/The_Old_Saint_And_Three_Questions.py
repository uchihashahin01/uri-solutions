for _ in range(int(input())):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    if a.count(1) == b.count(1):
        print("Pass")
    else:
        print("Fail")