import csv

ingredient_data = []
with open('day_5_cafeteria/ingredients.csv', newline='') as file: 
    ingredients_csv = csv.reader(file, delimiter=' ')
    for ingredient in ingredients_csv:
        if ingredient == []:
            ingredient_data.append('---')
            continue
        ingredient_data.append(ingredient[0])

# ingredient_data = [
#     '3-5',
#     '10-14',
#     '16-20',
#     '12-18',
#     '---',
#     '1',
#     '5',
#     '8',
#     '11',
#     '17',
#     '32',
# ]

fresh_ingredient_ranges = []
ingredients = []
index = 0
for i in range(0, len(ingredient_data)):
    if ingredient_data[i] == '---':
        index = i
        break
    fresh_ingredient_ranges.append(ingredient_data[i])
for i in range(index + 1, len(ingredient_data)):
    ingredients.append(ingredient_data[i])
        
fresh_ingredient_count = 0
for ingredient in ingredients:
    for fresh_ingredient_range in fresh_ingredient_ranges:
        start = int(fresh_ingredient_range.split('-')[0])
        end = int(fresh_ingredient_range.split('-')[1])
        if int(ingredient) >= start and int(ingredient) <= end:
            fresh_ingredient_count += 1
            break
        
print(fresh_ingredient_count)