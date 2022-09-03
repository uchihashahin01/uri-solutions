def total_mark(num1,num2):
    return ((num1-num2)*-1)+(num2*3)


def pass_or_fail(num3,num1,num2):
    if total_mark(num1,num2) >= num3:
        print("PASS")
    else:
        print("FAIL")

for _ in range(int(input())):
    total_question,correct_ans,marks_to_pass = list(map(int,input().split()))
    pass_or_fail(num1=total_question,num2=correct_ans,num3=marks_to_pass)
    

    
    