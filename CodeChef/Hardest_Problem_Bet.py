def minimum(a,b,c):
    return min(a,b,c)

def win(a,b,c):
    if minimum(a,b,c) == a:
        print("Draw")
    elif minimum(a,b,c) == b:
        print("Bob")
    elif minimum(a,b,c) == c:
        print("Alice")

for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))

    win(a,b,c)