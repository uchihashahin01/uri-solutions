for _ in range(int(input())):
    nitin,sobhagya,ritik,satyarth = list(map(int, input().split()))
    
    if nitin == sobhagya:
        print("N")   
    
    else:
        if nitin > sobhagya:
            sobhagya += ritik
        else:
            nitin += ritik
        
        if sobhagya > nitin:
            nitin += satyarth
        else:
            sobhagya += satyarth
    
        if nitin > sobhagya:
            print("N")
        else:
            print("S")
        
    