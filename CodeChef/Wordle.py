


for _ in range(int(input())):
    a = input()
    b = input()
    emp = ""
    for i in range(len(a)):
        
        if a[i] == b[i]:
            emp += 'G'
        else:
            emp += 'B'
    

    print(emp)