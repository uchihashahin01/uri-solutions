def rule107(num):
    return num * 1.07


def func(num1,num2):
    if rule107(num1)< num2:
        print("NO")
    else:
        print("YES")


for _ in range(int(input())):
    n = list(map(int,input().split()))

    func(n[0],n[1])