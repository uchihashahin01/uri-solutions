for _ in range(int(input())):
    x = []
    y = []
    a = list(map(str,input().split()))

    for i in range(len(a)):
        if i%2 == 0:
            x.append(a[i])
        else:
            y.append(a[i])
    
    if x.count('1') > y.count('1'):
        print("1")
    elif x.count('1') < y.count('1'):
        print("2")
    else:
        print("0")

# n = int(input())
# for i in range(n):
#     a = list(map(int, input().split()))
#     odd_i = a[::2]
#     even_i = a[1::2]
#     b = odd_i.count(1)
#     c = even_i.count(1)

#     if b > c:
#         print("1")
#     elif b < c:
#         print("2")
#     elif b == c:
#         print("0")