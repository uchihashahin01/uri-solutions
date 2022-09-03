for _ in range(int(input())):
    a = int(input())
    b = list(map(int,input().split())) 
    c = input()
    new_list = [] 
    for i in range(len(b)):
        if c[i] == '0':
            new_list.append(b[i])            
    
    ans = min(new_list)
    print(ans)