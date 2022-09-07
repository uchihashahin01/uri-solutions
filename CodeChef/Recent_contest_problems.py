for _ in range(int(input())):
    count1 = 0
    count2 = 0
    a = int(input())
    b = list(map(str,input().split()))[:a]

    count1 = sum(item == 'LTIME108' for item in b)
    count2 = sum(item == 'START38' for item in b)
        
    print(f"{count2} {count1}")