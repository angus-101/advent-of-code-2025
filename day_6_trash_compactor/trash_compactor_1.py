import csv

problems_raw = []
with open('day_6_trash_compactor/problems.csv', newline='') as file: 
    problems_csv = csv.reader(file, delimiter=' ')
    for row in problems_csv:
        row_raw = []
        for number_or_operation in row:
            if number_or_operation == '':
                continue
            row_raw.append(number_or_operation)
        problems_raw.append(row_raw)
        
answers_total = 0
for problem in range(0, len(problems_raw[0])):
    operator = problems_raw[-1][problem]
    answer = int(problems_raw[0][problem])
    for number in range(1, len(problems_raw) - 1):
        if operator == '+':
            answer += int(problems_raw[number][problem])
        elif operator == '*':
            answer *= int(problems_raw[number][problem])
    answers_total += answer
    
print(answers_total)