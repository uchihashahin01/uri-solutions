
def factorial(num):
    # 1 2 3 4 5
    result = 1
    for i in range(1, num+1):
        result = result * i
        
    return result

for _ in range(int(input())):
    a = int(input())
    
    print(factorial(a))
