for _ in range(int(input())):
    a = int(input())
    b = list(map(int,input().split()))
    # count = sum(b[i] >= 10 and b[i]<= 60 for i in range(a))
    count = 0
    for i in range(a):
        if b[i] >= 10 and b[i]<= 60:
            count += 1
    print(count)