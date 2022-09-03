user_input = int(input())
list1 = [user_input]
x = input().split(" ")
score = ""

for y in range(user_input):
    list1.append(x)
    y = x[-1]
    score += y
    
if int(score) % 10 == 0:
    print("Yes")
else:
    print("No")