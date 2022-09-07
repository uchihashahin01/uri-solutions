a = list(map(int,input().split()))
count = sum(item >= 10 for item in a)
print(count)