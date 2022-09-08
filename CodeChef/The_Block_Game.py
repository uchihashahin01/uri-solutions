for _ in range(int(input())):
    a = input()

    reverse = a[::-1]
    
    if a == reverse:
        print("wins")
    else:
        print('loses')
    
    