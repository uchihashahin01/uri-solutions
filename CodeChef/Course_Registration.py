def func(num1,num2,num3):
    if (num1 + num3 < num2 or num1 + num3 == num2):
        print("Yes")
    else:
        print("No")

for _ in range(int(input())):
    n = list(map(int,input().split()))

    func(n[0],n[1],n[2])