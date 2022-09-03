
for _ in range(int(input())):
    a = int(input())
    x = a % 4
    if x == 0:
        print("North")
    elif x == 1:
        print("East")
    elif x == 2:
        print("South")
    else:
        print("West")