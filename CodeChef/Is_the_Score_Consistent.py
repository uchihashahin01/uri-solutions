def first(num1,num2,num3,num4):
    if (num3 < num1 or num4 < num2):
        print("IMPOSSIBLE")    
    else:
        print("POSSIBLE")


user_input = int(input())

for _ in range(user_input):
    first_half = list(map(int,input().split()))
    second_half = list(map(int,input().split()))
    
    first(first_half[0],first_half[1],second_half[0],second_half[1])
    