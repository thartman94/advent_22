total = 0
with open("./input-3.txt") as file:
    lines = file.readlines()


def get_val(char):
    tmp = ord(char)
    return tmp - 38 if tmp <= 90 else tmp - 96


for line in lines:
    first = line[: (len(line) // 2)]
    second = line[len(line) // 2 :]
    for f in first:
        if f in second:
            total += get_val(f)
            break

print(total)
