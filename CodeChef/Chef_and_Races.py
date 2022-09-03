for _ in range(int(input())):
    a,b,c,d = list(map(str,input().split()))

    chef = [a,b]
    opponent = [c,d]
    count = 2

    if a in [c, d]:
        count -=1
    if b in [c, d]:
        count -=1

#    if a == c or a == d:
#         count -=1
#     if b== c or b ==d:
#         count -=1
    print(count)