summary = 0
with open('income.csv') as handler:
    for line in handler:
        line_arr = line.strip().split(',')
        created, desc, value = line_arr
        summary += int(value)

print(summary)
