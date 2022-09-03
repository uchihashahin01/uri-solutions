#
## num1 = Total Bottle 
## num2 = Bottle Capacity
## num3 = Tank Capacity

def func(num1, num2, num3):
    
    if num2 > num3:
        print("0")
        
    elif num1 > num3 / num2:
        print(int(num3 / num2))
        
    elif num1 < num3 / num2:
        print(num1)

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))

    func(a,b,c)