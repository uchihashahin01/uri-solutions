n = int(input())
num_list = list(int(num) for num in input().strip().split())[:n]
new_list = list(set(num_list))
new_list.sort()

print(new_list[-2])