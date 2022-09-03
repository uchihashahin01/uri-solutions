# def holidays():
#     month = 30
#     saturday = 6
#     sunday = 7
#     saturday_count = 0
#     sunday_count = 0
    
#     for _ in range(month):
#         if (saturday + 7) <= 31:
#             saturday_count +=1
#         if (sunday + 7) <= 31:
#             sunday_count +=1

#     return saturday_count + sunday_count

for _ in range(int(input())):
    a = int(input())
    b = list(map(int,input().split()))
    
    c = []
    for i in range(len(b)):
        c.append(b[i])
    for i in range(6,30,7):
        c.append(i)
    for i in range(7,30,7):
        c.append(i)
    for i in c:
        if i in c:
            continue
        else:
            c.append(i)
    new_list = list(dict.fromkeys(c))
    print(len(new_list))
    
# n = int(input())
# for _ in range(n):
#     x = int(input())
#     y = list(map(int, input().split()))
#     z = [6, 7, 13, 14, 20, 21, 27, 28]
#     count = 8
#     for i in y:
#         if i not in z:
#             count += 1
#         else :
#             count += 0
#     print(count)