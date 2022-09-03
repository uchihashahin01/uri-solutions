

for _ in range(int(input())):

    height, weight = list(map(int,input().split()))


    bmi = height / (weight)**2
    
    if bmi <= 18:
        print("1")
    elif bmi <= 24:
        print("2")
    elif bmi <= 29:
        print("3")
    else:
        print("4")