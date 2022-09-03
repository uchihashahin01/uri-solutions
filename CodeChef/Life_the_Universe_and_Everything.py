# def stop(num):
#     while(num != 42):
#         print(num)
#         if (num==42):
#             break


try:
    b = True

    while(b):
        a = int(input())
        if a == 42:
            b = False
        else:
            print(a)
except:
    pass