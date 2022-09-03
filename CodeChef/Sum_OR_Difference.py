try:
    def my_func(a,b):
        if (a > b):
            print(a - b)
        else:
            print(a +b)    

    a = int(input())
    b = int(input())

    my_func(a,b)
    
except:
    pass