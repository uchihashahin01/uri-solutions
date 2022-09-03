# 1 <100 easy
# 100 <200 medium
# 200<=300 hard

def my_func(a):
    if a < 100:
        print("Easy")
    elif a < 200:
        print("Medium")
    elif a <= 300:
        print("Hard")
    
for _ in range(int(input())):
    a = int(input())
    my_func(a)