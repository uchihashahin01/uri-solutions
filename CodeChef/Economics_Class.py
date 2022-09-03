for _ in range(int(input())):
    # for _ in range(int(input())):
        c = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        count = 0
        for i in range(c):
            if a[i] == b[i]:
                count += 1
            i += 1
        print(count)