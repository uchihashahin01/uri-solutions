def highest(num1):
    return max(num1)


for _ in range(int(input())):
    n = list(map(int,input().split()))

    print(highest(n))
    # print(max(n))