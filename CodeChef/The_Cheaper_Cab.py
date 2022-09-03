for _ in range(int(input())):
    user_inp = list(map(int,input().split())) 

    lowest = user_inp[0]
    if user_inp[1] < lowest:
        lowest = user_inp[1]
        print("SECOND")

    elif lowest == user_inp[1]:
        print("ANY")

    else:
        print("FIRST")

