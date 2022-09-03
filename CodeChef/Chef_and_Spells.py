def my_func(a):
    sorted_a = sorted(a)
    
    print(sorted_a[-1] + sorted_a[-2])
    
for _ in range(int(input())):
    a = list(map(int,input().split()))
    my_func(a)