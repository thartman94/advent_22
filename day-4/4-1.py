acc = 0
with open("./input-4.txt") as file:
    pairs = file.readlines()


def make_elf(data):
    elf = {"start": int(data.split("-")[0])}
    elf["end"] = int(data.split("-")[1])
    elf["range"] = elf["end"] - elf["start"]
    return elf


def inc_if_contains(large_elf, small_elf):
    return small_elf["start"] >= large_elf["start"] and small_elf["end"] <= large_elf["end"]


for pair in pairs:
    pair = pair.strip().split(",")
    elf_1, elf_2 = make_elf(pair[0]), make_elf(pair[1])
    acc += inc_if_contains(elf_1, elf_2) if elf_1["range"] > elf_2["range"] else inc_if_contains(elf_2, elf_1)

print(acc)
