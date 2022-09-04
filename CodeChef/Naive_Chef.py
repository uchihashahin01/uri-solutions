for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    e = 0
    f = 0

    for item in d:
        if item == b:
            e+=1
        if item == c:
            f+=1

    ans = float((e/a)*(f/a))
    print(ans)