# Overload semester if the number of credits taken \gt 65>65.
# Underload semester if the number of credits taken \lt 35<35.
# Normal semester otherwise

def func(a):
    if a > 65:
        print("Overload")
    elif a < 35:
        print("Underload")
    else:
        print("Normal")


for _ in range(int(input())):
    a = int(input())
    func(a)