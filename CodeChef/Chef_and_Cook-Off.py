# A contestant that solved exactly 0 problems is a beginner.
# A contestant that solved exactly 1 problem is a junior developer.
# A contestant that solved exactly 2 problems is a middle developer.
# A contestant that solved exactly 3 problems is a senior developer.
# A contestant that solved exactly 4 problems is a hacker.
# A contestant that solved all five problems is Jeff Dean.

def my_func(a):
    x = a.count(1)
    
    if x == 0:
        print("Beginner")
    elif x == 1:
        print("Junior Developer")
    elif x == 2:
        print("Middle Developer")
    elif x == 3:
        print("Senior Developer")
    elif x == 4:
        print("Hacker")
    elif x == 5:
        print("Jeff Dean")
        
for _ in range(int(input())):    
    a = list(map(int,input().split()))
    my_func(a)