student_marks = {}
result = 0
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

if query_name in student_marks:
    for i in student_marks[query_name]:
        result += i
    print(format(result/3, '.2f'))