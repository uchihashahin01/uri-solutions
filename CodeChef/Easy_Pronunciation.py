# for _ in range(int(input())):
#     a = int(input())
#     b = input()
#     consonant = 0
#     x = 0
#     for i in range(a):
#         if consonant == 4:
#             x = 1
#             break
#         if b[i] in ['a', 'e', 'i', 'o', 'u']:
#             consonant = 0

#         else:
#             consonant+=1
        
#     if x == 0:
#         print("YES")
#     else:
#         print("NO")



for _ in range(int(input())):
    a = int(input())
    b = input()
    consonant = 0
    x = 0
    for i in range(a): 
        if b[i] in ['a', 'e', 'i', 'o', 'u']:
            consonant = 0
        else:
            consonant += 1
            if consonant >= 4:
                x = 1
                break
    if x >= 1:
        print("NO")
    else:
        print("YES")