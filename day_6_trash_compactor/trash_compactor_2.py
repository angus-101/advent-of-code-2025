import csv

problems_raw = []
with open('day_6_trash_compactor/problems.csv', newline='') as file: 
    problems_csv = csv.reader(file, delimiter=' ')
    for row in problems_csv:
        numbers = []
        for number in row:
            if number == '':
                numbers.append(' ')
            else:
                for digit in number:
                    numbers.append(digit)
        problems_raw.append(numbers)

sizes = []
operations_raw = problems_raw[-1]
operations = []
for operation_raw in range(0, len(operations_raw)):
    if operations_raw[operation_raw] == '+' or operations_raw[operation_raw] == '*':
        operations.append(operations_raw[operation_raw])
        size = 1
        for space in range(operation_raw + 1, len(operations_raw)):
            if operations_raw[space] != ' ':
                break
            size += 1
        sizes.append(size)

numbers = []
for row_index in range(0, len(problems_raw) - 1):
    row_raw = problems_raw[row_index]
    row = []
    row_progress = 0
    for size in sizes:
        number = ''.join(row_raw[row_progress:row_progress + size])
        row.append(number)
        row_progress += size
    numbers.append(row)
    
total = 0
for number_index in range(0, len(numbers[0])):
    problem_total = 0
    size = sizes[number_index]
    for size_index in range(size - 1, -1, -1):
        number = ''
        for row_index in range(0, len(numbers)):
            if numbers[row_index][number_index][size_index] == ' ':
                continue
            number += numbers[row_index][number_index][size_index]
        if operations[number_index] == '*':
            if problem_total == 0:
                problem_total = 1
            problem_total *= int(number)
        else:
            problem_total += int(number)
    total += problem_total

print(total)
        