for _ in range(int(input())):
    a = int(input())
    b = list(map(int,input().split()))[:a]
            
    count = sum(item >= 1000 for item in b)
    print(count)