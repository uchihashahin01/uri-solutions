def shoes(num1,num2):
    if num1<=num2:
        print(num1)
        
    else:
        print(num2+ (num1-num2)*2)
        
    

for _ in range(int(input())):
    n = list(map(int,input().split())) 

    
    shoes(n[0],n[1])