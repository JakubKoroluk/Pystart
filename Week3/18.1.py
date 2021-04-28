tuples = [
    (1,),
    (1, 2, 4),
    (2, 4, 5, 1),
    (1, 5, 12, 10),
    (6, 1, 34, 234, 123, 15, 67)
]
list2 = 0

filtered = [sum(item) if len(item) % 2 == 0 else sum(item) / len(item)  for item in tuples if 7 > len(item) > 1]
print(filtered)



