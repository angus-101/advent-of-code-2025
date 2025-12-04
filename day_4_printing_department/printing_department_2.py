import csv

rolls = []
with open('day_4_printing_department/rolls.csv', newline='') as file: 
    rolls_csv = csv.reader(file, delimiter=' ')
    for roll in rolls_csv:
        rolls.append(roll[0])
        
def remove_rolls(rolls):
    removed_rolls = 0
    for row in range(0, len(rolls)):
        for roll in range(0, len(rolls[row])):
            roll_count = 0
            if rolls[row][roll] == '@':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if row + i < 0 or row + i > len(rolls) - 1 or roll + j < 0 or roll + j > len(rolls[row]) - 1:
                            # Ignore out of bounds neighbours
                            continue
                        if rolls[row + i][roll + j] == '@':
                            roll_count += 1
                if roll_count < 4:
                    removed_rolls += 1
                    rolls[row] = rolls[row][:roll] + '.' + rolls[row][roll + 1:]
    return rolls, removed_rolls

removed_rolls = 1
total_removed_rolls = 0
while removed_rolls > 0:
    rolls, removed_rolls = remove_rolls(rolls)
    total_removed_rolls += removed_rolls
                
print(total_removed_rolls)