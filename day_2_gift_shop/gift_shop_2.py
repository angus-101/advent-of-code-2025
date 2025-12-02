import csv

with open('day_2_gift_shop/ids.csv', newline='') as file: 
    ids_csv = csv.reader(file, delimiter=',')
    for id in ids_csv:
        ids = id

id_count = 0
for id_range in ids:
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])
    for id in range(start, end + 1):
        id_str = str(id)
        id_digits = len(id_str)
        for factor in range(1, id_digits // 2 + 1):
            # Can only have repeated sequences of numbers that have digits equal to
            # the factors of the ID
            if len(id_str) % factor != 0:
                continue
            # Split the ID into parts of length factor
            parts = [id_str[i:i+factor] for i in range(0, len(id_str), factor)]
            # Converting list to set removes duplicates
            if len(set(parts)) == 1:
                id_count += id
                break
print(id_count)