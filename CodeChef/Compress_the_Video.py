from itertools import count


for _ in range(int(input())):
    a = int(input())
    
    b = list(map(int,input().split()))[:a]
    
    if a == 1:
        print("1")
    
    else:
        count = len(b)
        for i in range(count - 1):
            if b[i] == b[i + 1]:
                count -= 1
        print(count)