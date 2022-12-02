file = open("./input-1.txt")
max_cal = 0
current_cal = 0

for line in file.readlines():
    if line == "\n":
        max_cal = max(max_cal, current_cal)
        current_cal = 0
    else:
        current_cal += int(line)


print(max_cal)
