def choice(num1,num2):
    if num1 == '0':
        print("https://www.codechef.com/practice")
    elif num2 == '0':
        print("https://www.codechef.com/contests")
        
    else:
        print("https://discuss.codechef.com")
        
a,b = list(map(str,input().split()))

choice(a,b)
    