# In a company an emplopyee is paid as under: If his basic salary is less than Rs. 1500, then HRA = 10% of base salary and DA = 90% of basic salary.
# If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the Employee's salary is input, write a program to find his gross salary.

# NOTE: Gross Salary = Basic Salary + HRA + DA

def my_func(a):
    if a < 1500:
        print((0.1 * a)+(0.9 * a)+a)
    
    elif a >= 1500:
        print(500+(0.98 * a)+a)

for _ in range(int(input())):
    a = int(input())

    my_func(a)