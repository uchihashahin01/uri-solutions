def my_func(a,b,c):

    if a > c:
        print("Too Late")
    elif a < b:
        print("Too Early")
    else:
        print("Take second dose now")

for _ in range(int(input())):
    
    a,b,c = list(map(int,input().split()))

    my_func(a,b,c)