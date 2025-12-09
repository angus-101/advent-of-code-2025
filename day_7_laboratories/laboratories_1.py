import csv

manifold = []
with open('day_7_laboratories/manifold.csv', newline='') as file: 
    manifold_csv = csv.reader(file, delimiter=' ')
    for row in manifold_csv:
        manifold.append(row[0])

splits = 0
for row_index in range(1, len(manifold)):
    for point_index in range(0, len(manifold[row_index])):
        if manifold[row_index - 1][point_index] == 'S':
            manifold[row_index] = manifold[row_index][:point_index] + '|' + manifold[row_index][point_index + 1:]
        elif manifold[row_index - 1][point_index] == '|':
            if manifold[row_index][point_index] == '^':
                splits += 1
                manifold[row_index] = manifold[row_index][:point_index - 1] + '|' + manifold[row_index][point_index:]
                manifold[row_index] = manifold[row_index][:point_index + 1] + '|' + manifold[row_index][point_index + 2:]
            else:
                manifold[row_index] = manifold[row_index][:point_index] + '|' + manifold[row_index][point_index + 1:]

print(splits)