n,m = list(map(int,input().split()))
count = 0

for _ in range(n):
    o = int(input())
    if o % m == 0:
        count += 1
    
print(count)
    

# codechef solution
# # We have populated the solutions for the 10 easiest problems for your support.
# # Click on the SUBMIT button to make a submission to this problem.
# #Note that it's python3 Code. Here, we are using input() instead of raw_input().
# #You can check on your local machine the version of python by typing "python --version" in the terminal.

# (n, k) = map(int, input().split(' '))

# ans = 0

# for i in range(n):
# 	x = int(input())
# 	if x % k == 0:
# 		ans += 1

# print(ans)	
