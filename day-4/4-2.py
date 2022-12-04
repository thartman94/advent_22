acc = 0
with open("./input-4.txt") as file:
    pairs = file.readlines()


def make_elf(data):
    elf = {"start": int(data.split("-")[0])}
    elf["end"] = int(data.split("-")[1])
    return elf


def check_overlap(elf_1, elf_2):
    return elf_1["end"] >= elf_2["start"] and elf_2["end"] >= elf_1["start"]


for pair in pairs:
    pair = pair.strip().split(",")
    elf_1, elf_2 = make_elf(pair[0]), make_elf(pair[1])
    acc += check_overlap(elf_1, elf_2)

print(acc)
