import csv

manifold = []
with open('day_7_laboratories/manifold.csv', newline='') as file: 
    manifold_csv = csv.reader(file, delimiter=' ')
    for row in manifold_csv:
        manifold.append(list(row[0]))

for row_index in range(1, len(manifold)):
    for point_index in range(0, len(manifold[row_index])):
        if manifold[row_index - 1][point_index] == 'S':
            # Case for source producing a path
            manifold[row_index][point_index] = '1'
        elif manifold[row_index - 1][point_index] not in ['S', '.', '^']:
            # Case for if there is a path above this point
            path_count = manifold[row_index - 1][point_index]
            if manifold[row_index][point_index] == '^':
                # Case for if the path meets a splitter
                if manifold[row_index][point_index - 1] == '.':
                    # Case for if this is the first path to reach the point left of the splitter
                    manifold[row_index][point_index - 1] = path_count
                else:
                    # Case for different paths meeting at the same point left of the splitter
                    path_count_new = int(manifold[row_index][point_index - 1]) + int(path_count)
                    manifold[row_index][point_index - 1] = str(path_count_new)
                if manifold[row_index][point_index + 1] == '.':
                    # Case for if this is the first path to reach the point right of the splitter
                    manifold[row_index][point_index + 1] = path_count
            else:
                if manifold[row_index][point_index] == '.':
                    # Case for path continuing down without meeting another path
                    manifold[row_index][point_index] = path_count
                else:
                    # Case for stright path meeting split path
                    path_count_new = int(manifold[row_index][point_index]) + int(path_count) 
                    manifold[row_index][point_index] = str(path_count_new)

universes = 0
for number in manifold[-1]:
    if number not in ['.', '^']:
        universes += int(number)
        
print(universes)