import csv

with open('day_2_gift_shop/ids.csv', newline='') as file: 
    ids_csv = csv.reader(file, delimiter=',')
    for id in ids_csv:
        ids = id

id_count = 0
for id_range in ids:
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])
    start_digits = len(str(start))
    end_digits = len(str(end))
    # Cannot have a repeated sequence in an ID with an odd number of digits
    if start_digits % 2 == 1 and end_digits % 2 == 1 and end / start < 10:
        continue
    for id in range(start, end + 1):
        id_str = str(id)
        # Cannot have a repeated sequence in an ID with an odd number of digits
        if len(id_str) % 2 == 1:
            continue
        # We know that every ID will have an even number of digits so can split them in two
        first_half, second_half = id_str[:len(id_str)//2], id_str[len(id_str)//2:]
        if first_half == second_half:
            id_count += id
print(id_count)