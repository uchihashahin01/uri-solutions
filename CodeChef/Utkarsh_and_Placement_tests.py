for _ in range(int(input())):
    a = list(map(str,input().split()))
    b = list(map(str,input().split()))

    if a[0] in b:
        print(a[0])
    else:
        print(a[1])