def bigsum(num1,num2):
    if num1 > num2:
        print(num1-num2)
    
    else:
        print(num2-num1)

for _ in range(int(input())):
    u_inp = list(map(int,input().split())) 
    
    bigsum(u_inp[0],u_inp[1])