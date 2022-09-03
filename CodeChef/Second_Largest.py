def second_large(a):
    a.sort()
        
    return a[-2]

for _ in range(int(input())):
    a = list(map(int,input().split()))
    # a.sort()
    print(second_large(a))