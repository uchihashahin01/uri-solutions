for _ in range(int(input())):
    a ,b = list(map(int,input().split()))

    top10 = a * 10
    rest_of_all = b * 90
    
    print(top10 + rest_of_all)