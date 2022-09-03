def  my_func(a,b,c,d,e,f):
    count_a = 0
    count_b = 0
    if a>b:
        count_a += 1
    else:
        count_b += 1
    if c>d:
        count_a += 1
    else:
        count_b += 1
    if e>f:
        count_a += 1
    else:
        count_b += 1
    
    if count_a > count_b:
        print("A")
    else:
        print("B")

        
for _ in range(int(input())):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    my_func(a=a[0],b=b[0],c=a[1],d=b[1],e=a[2],f=b[2])