# S = input()

# reverse = S[::-1]

# if (S == reverse):
#     print("YES")
# else:
#     print("NO")


s= input()
x=[i for i in s]
list2 = x.copy()
list2.reverse()

 
if x == list2:
    print("YES")
else:
    print("NO")

# copy_list.reverse()
 

# if main_list == copy_list:
#     print("Palindrome")
# else:
#     print("Not Palindrome")