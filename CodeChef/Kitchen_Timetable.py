try:
    def my_func(a,b,k):
        count = 0
        if a[0] >= b[0]:
            count += 1
            
        for i in range(k-1):
            if a[i+1] - a[i] >= b[i+1]:
                count += 1
        return print(count)
            

    for _ in range(int(input())):
        k = int(input())

        a = list(map(int,input().split()))[:k]
        b = list(map(int,input().split()))[:k]
        
        my_func(a=a,b=b,k=k)

except:
    pass