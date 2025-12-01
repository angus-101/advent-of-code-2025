import csv

rotations = []
with open('day_1_secret_entrance/rotations.csv', newline='') as file: 
    rotations_csv = csv.reader(file, delimiter=' ')
    for rotation in rotations_csv:
        rotations.append(rotation[0])

def secret_entrance(rotations):
    position = 50
    end_zeroes = 0
    rotation_zeroes = 0
    for rotation in rotations:
        direction = rotation[0]
        magnitude = int(rotation[1:])
        new_position = position + magnitude if direction == 'R' else position - magnitude
        new_zeroes = 0
        if new_position < 0:
            new_zeroes = (abs(new_position) + 100) // 100
            # Start and end on 0 case (two double counted zeroes)
            if position == 0 and new_position % 100 == 0:
                new_zeroes -= 2
            # Start or end on 0 case (one double counted zero)
            elif position == 0 or new_position % 100 == 0:
                new_zeroes -= 1
        elif new_position > 0:
            new_zeroes = new_position // 100
            # End on zero case (one double counted zero)
            if new_position % 100 == 0:
                new_zeroes -= 1
        rotation_zeroes += new_zeroes
        position = new_position % 100
        if position == 0:
            end_zeroes += 1
    return end_zeroes + rotation_zeroes

zeroes = secret_entrance(rotations)
print('total zeroes: ' + str(zeroes))
