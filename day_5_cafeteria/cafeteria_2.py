import csv

ranges = []
with open('day_5_cafeteria/ingredients.csv', newline='') as file: 
    ingredients_csv = csv.reader(file, delimiter=' ')
    for id_range in ingredients_csv:
        if id_range == []:
            break
        ranges.append(id_range[0])

def get_range_start(range):
    return int(range.split('-')[0])

def get_range_end(range):
    return int(range.split('-')[1])

# 'Turn around' any ranges that are in reverse order
for range_index in range(0, len(ranges)):
    id_range = ranges[range_index]
    start = get_range_start(id_range)
    end = get_range_end(id_range)
    if end < start:
        ranges[range_index] = str(end) + '-' + str(start)

# sort ranges by starting ID
sorted_ranges = sorted(ranges, key=get_range_start)
 
range_index = 0
while range_index < len(sorted_ranges):
    interval = sorted_ranges[range_index]
    start = get_range_start(interval)
    end = get_range_end(interval)
    if range_index == len(sorted_ranges) - 1:
        # Either the last range was merged into the second to last,
        # or the last is a range on its own 
        break
    next_interval = sorted_ranges[range_index + 1]
    next_start = get_range_start(next_interval)
    next_end = get_range_end(next_interval)
    if start <= next_start and end >= next_end:
        # Case for current range completely encompassing next range
        sorted_ranges.pop(range_index + 1)
        continue
    if next_start <= end + 1:
        # Case for current range partially encompassing next range
        sorted_ranges.pop(range_index + 1)
        sorted_ranges[range_index] = str(start) + '-' + str(next_end)
        continue
    range_index += 1
    
total_fresh_ids = 0
for interval in sorted_ranges:
    start = get_range_start(interval)
    end = get_range_end(interval)
    fresh_ids = end - start + 1
    total_fresh_ids += fresh_ids
    
print(total_fresh_ids)
    