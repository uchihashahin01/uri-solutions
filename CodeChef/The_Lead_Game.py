total_player1 = 0
total_player2 = 0

new_list = [0,0]
# lead = 0
# win_player = 0

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    
    total_player1 += a
    total_player2 += b
    
    if (total_player1 > total_player2):
        # print("1")
        # print(f"{total_player1}")
        new = total_player1 - total_player2
        if new > new_list[1]:
            new_list[1] = new
            new_list[0] = 1
            # print(f"1 {lead}")
    else:
        new = total_player2 - total_player1
        if new > new_list[1]:
            new_list[1] = new
            new_list[0] = 2
            # print(f"2 {lead}")
print(f"{new_list[0]} {new_list[1]}")
    
    