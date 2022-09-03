
from posixpath import split


for _ in range(int(input())):
    count1 = 0
    count2 = 0

    
    a = list(map(int,input().split()))
    for i in range(7):
        if a[i] == 1:
            count1 += 1
            i+=1
        else:
            count2 += 1
            i+=1
    if count1 > count2:
        print("YES")
    else:
        print("NO")


# n = int(input())
# for i in range(n):
#     x = list(map(int, input().split()))
#     y = x.count(1)
#     z = x.count(0)
#     if y>z :
#         print("YES")
#     else :
#         print("NO")

    