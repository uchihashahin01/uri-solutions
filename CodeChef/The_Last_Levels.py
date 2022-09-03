def break_time(num1,num3):
    
    if num1%3==0:
        return (num3*int((num1-3)/3))
    else:
        return (num3*int(num1/3))

def time(a,b,c):
    if a<=3:
        print(a*b)

    else:
        print(b *a + (break_time(a,c)))

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    
    time(a,b,c)