def years():
    return [2010,2015,2016,2017,2019]

def my_func(a):
    if a not in years():
        print("NOT HOSTED")
    else:
        print("HOSTED")
        
for _ in range(int(input())):
    a = int(input())
    
    my_func(a)