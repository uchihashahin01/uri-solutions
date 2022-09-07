for _ in range(int(input())):
    a,b = map(int,input().split())
    count = 0
    for i in range(a,b+1):
        c = str(i)
        if c[-1] in ['2', '3', '9']:
            count += 1


    print(count)