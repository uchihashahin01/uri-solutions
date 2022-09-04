n = int(input())
for _ in range(n):
    nitin,sobhagya,ritik,satyarth = list(map(int, input().split()))
    
    
    if nitin >= sobhagya:
        sobhagya += ritik
        
        if sobhagya > nitin:
            nitin += satyarth
        else:
            sobhagya += satyarth
        
        if sobhagya > nitin:
            print("S")
        else:
            print("N")
    
    else:
        nitin += ritik
        if sobhagya > nitin:
            nitin += satyarth
        else:
            sobhagya += satyarth
        
        
        if sobhagya > nitin:
            print("S")
        else:
            print("N")