for _ in range(int(input())):
    a ,b ,c = list(map(int, input().split()))
    
    calc = b + (100 - a) * c
    
    print(calc * 10)