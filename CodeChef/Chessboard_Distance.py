def diff(a,b,c,d):
    return print(max(abs(a-c),(b-d)))


for _ in range(int(input())):
    a,b,c,d = list(map(int,input().split()))
    
    diff(a,b,c,d)