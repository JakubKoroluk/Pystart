# from csv import reader, writer
#
# result = []
# with open('transakcje.csv') as input_file:
#     content = reader(input_file, delimiter=',')
#     next(content)
#     for line in content:
#         created_ad, description, value = line
#         if int(value) > 0:
#             result.append(line)
#
# with open('income.csv', 'w', newline='') as output_file:
#     content = writer(output_file, delimiter=',')
#     for line in result:
#         content.writerow(line)

result = []
with open('transakcje.csv') as input_file:
    next(input_file)
    for line in input_file:
        line_as_list = line.strip().split(',')
        created_at, desc, value = line_as_list
        if int(value) > 0:
            result.append(line)

print(result)

with open('income1.csv', 'a') as output_file:
    output_file.writelines(result)
