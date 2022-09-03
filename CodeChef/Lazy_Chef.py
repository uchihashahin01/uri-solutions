def time(a,b,c):
    return print(min(a*b,a+c))

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    
    time(a,b,c)