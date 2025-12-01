import csv

rotations = []
with open('rotations.csv', newline='') as file: 
    rotations_csv = csv.reader(file, delimiter=' ')
    for rotation in rotations_csv:
        rotations.append(rotation[0])

position = 50
zeroes = 0
for rotation in rotations:
    direction = rotation[0]
    magnitude = int(rotation[1:])
    new_position = position + magnitude if direction == 'R' else position - magnitude
    position = new_position % 100
    if position == 0:
        zeroes += 1

print(zeroes)
