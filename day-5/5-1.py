def transpose(state):
    temp = []
    for row in range(len(state) - 1, -1, -1):
        for i, item in enumerate(state[row]):
            if len(temp) < i + 1:
                temp.append([])
            if item != " ":
                temp[i].append(item)
    return temp


state = []
ans = ""
with open("./input.txt") as file:
    steps = file.readlines()

datastart = 0
for i, step in enumerate(steps):
    if "[" not in step:
        datastart = i + 2
        break
    state.append([])

    for j in range(0, len(step[:-1]), 4):
        state[i].append(step[j + 1])

state = transpose(state)

for step in range(datastart, len(steps)):
    work = steps[step].strip().split(" ")
    work = list(filter(lambda x: x.isnumeric(), work))

    work = {
        "count": int(work[0]),
        "from": int(work[1]) - 1,
        "to": int(work[2]) - 1,
    }

    for i in range(work["count"]):
        state[work["to"]].append(state[work["from"]].pop())

for line in state:
    ans += line.pop()

print(ans)
