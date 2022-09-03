try:
    n = int(input())
    even_count = 0
    odd_count = 0
    inp = list(map(int,input().split()))
    for i in range(n):
        if inp[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        i+=1

    if even_count > odd_count:
        print("READY FOR BATTLE")
    else:
        print("NOT READY")
except:
    pass