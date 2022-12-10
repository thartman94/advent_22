grid = []
with open("./input.txt") as file:
    grid.extend(line.strip() for line in file)

height = len(grid)
width = len(grid[0])
max_scenic = 0


def check_left(tree, h, w):
    i = w - 1
    count = 1

    while i > 0 and not grid[h][i] >= tree:
        i -= 1
        count += 1

    return count


def check_right(tree, h, w):
    i = w + 1
    count = 1

    while i < width - 1 and not grid[h][i] >= tree:
        i += 1
        count += 1

    return count


def check_up(tree, h, w):
    i = h - 1
    count = 1

    while i > 0 and not grid[i][w] >= tree:
        i -= 1
        count += 1

    return count


def check_down(tree, h, w):
    i = h + 1
    count = 1

    while i < height - 1 and not grid[i][w] >= tree:
        i += 1
        count += 1

    return count


def get_scenic_score(tree, h, w):
    return check_left(tree, h, w) * check_right(tree, h, w) * check_up(tree, h, w) * check_down(tree, h, w)


for h in range(1, height - 1):
    for w in range(1, width - 1):
        max_scenic = max(max_scenic, get_scenic_score(grid[h][w], h, w))


print(max_scenic)
