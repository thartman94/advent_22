total = 0
with open("./input-3.txt") as file:
    lines = file.readlines()


def get_val(char):
    tmp = ord(char)
    return tmp - 38 if tmp <= 90 else tmp - 96


for item_index in range(0, len(lines), 3):
    first = lines[item_index]
    second = lines[item_index + 1]
    third = lines[item_index + 2]

    for item in first:
        if item in second and item in third:
            total += get_val(item)
            break


print(total)
