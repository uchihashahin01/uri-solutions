name_score_list = []
score_list = []

for _ in range(int(input())):
        name_inp = input()
        score_inp = float(input())
        name_score_list.append([name_inp, score_inp])        
        score_list.append([score_inp])
        
#main inputted list 
# print(name_score_list)
# copy_list = name_score_list.copy()
# score list
# print(score_list)
name_score_list.sort()
#print(name_score_list)
second_lowesrt_score = name_score_list[1][-1]
# print(second_lowesrt_score)
for i,j in name_score_list:
    if j == second_lowesrt_score:
        print(i)
