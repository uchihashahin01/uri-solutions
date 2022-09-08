from typing import Counter


for _ in range(int(input())):
    a = int(input())

    b = list(map(int,input().split()))[:a]
    
    count = Counter(b)
    max_val = max(count.values())
    print(a - max_val)