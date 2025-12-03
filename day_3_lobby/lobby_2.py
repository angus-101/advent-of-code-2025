import csv

banks = []
with open('day_3_lobby/banks.csv', newline='') as file: 
    banks_csv = csv.reader(file, delimiter=' ')
    for bank in banks_csv:
        banks.append(bank[0])

def search_bank(bank):
    for i in range(9, -1, -1):
        for joltage in bank:
            if joltage == str(i):
                return joltage, bank.index(joltage)

total_joltage = 0
for bank in banks:
    max_joltage = ''
    for i in range(12, 0, -1):
        sub_bank_joltage, index = search_bank(bank[:len(bank) - (i - 1)])
        max_joltage += sub_bank_joltage
        bank = bank[index + 1:]
    total_joltage += int(max_joltage)
                
print(total_joltage)