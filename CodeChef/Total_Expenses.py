try:
    def calc(a,b):
        if a > 1000:
            print(a*b - (a*b*0.1))
        else:
            print(a*b)
        
    for _ in range(int(input())):
        a,b = list(map(float,input().split()))

        calc(a,b)
except:
    pass