def func(num1,num2):
    if (num1 > num2  or num1 == num2):
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    a = list(map(int,input().split()))
    
    func(a[0],a[1])




# Without Funtion
# for _ in range(int(input())):
#     a = list(map(int,input().split()))
    
#     if (a[0] > a[1]  or a[0] == a[1]):
#         print("YES")

#     else:
#         print("NO")