def my_func(a,b):
    summ = str(a + b)
    count = 0
    for i in range(len(summ)):
        if summ[i]=='0' or summ[i]=='6' or summ[i]=='9':
            count+=6
        if summ[i]=='2' or summ[i]=='3' or summ[i]=='5':
            count+=5
        if summ[i]=='1':
            count+=2
        if summ[i]=='4':
            count+=4
        if summ[i]=='7':
            count+=3
        if summ[i]=='8':
            count+=7
        
    print(count)

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    
    my_func(a,b)