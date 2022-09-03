
for _ in range(int(input())):
    a = int(input())
   
    total = 0
    for i in range(1,a+1):

        if i % 2 != 0:
            total +=3
        else:
            total -=1
    
    print(total)
    

# n = int(input())
# for i in range(n):
#     x = int(input())
#     if x%2==1:
#         print(x+2)
#     else :
#         print(x)