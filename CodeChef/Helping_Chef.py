try:
    def cond(a):
            if a < 10:
                print("Thanks for helping Chef!")
            else:
                print("-1")
                
    for _ in range(int(input())):
        a = int(input())

        cond(a)
        
except:
    pass
