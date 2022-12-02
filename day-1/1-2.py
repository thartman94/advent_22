import functools

file = open("./input-1.txt")
max_cals = []
current_cal = 0


def insert(current_cal):
    if len(max_cals) < 3:
        max_cals.append(current_cal)
        return
    for i, val in enumerate(max_cals):
        if current_cal > val:
            max_cals[i] = current_cal
            break


for line in file.readlines():
    if line == "\n":
        insert(current_cal)
        current_cal = 0
    else:
        current_cal += int(line)

file.close()

total = functools.reduce(lambda a, b: a + b, max_cals)
print(max_cals)
print(total)
