for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    count = sum(c[i] > b for i in range(a))
    print(count)