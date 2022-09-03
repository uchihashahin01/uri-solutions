def func(a,b,c):
    if b*c >= a:
        print("NO")
    else:
        print("YES")

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))

    func(a,b,c)