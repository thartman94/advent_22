grid = []
with open("./input.txt") as file:
    grid.extend(line.strip() for line in file)

height = len(grid)
width = len(grid[0])
visible = 2 * (height + width - 2)


def check_left(tree, h, w):
    i = 0
    blocked = False

    while i < w and not blocked:
        if grid[h][i] >= tree:
            blocked = True
        i += 1
    return not blocked


def check_right(tree, h, w):
    i = w + 1
    blocked = False

    while i < width and not blocked:
        if grid[h][i] >= tree:
            blocked = True
        i += 1
    return not blocked


def check_up(tree, h, w):
    i = 0
    blocked = False

    while i < h and not blocked:
        if grid[i][w] >= tree:
            blocked = True
        i += 1
    return not blocked


def check_down(tree, h, w):
    i = h + 1
    blocked = False

    while i < height and not blocked:
        if grid[i][w] >= tree:
            blocked = True
        i += 1
    return not blocked


def isVisible(tree, h, w):
    return check_left(tree, h, w) or check_right(tree, h, w) or check_up(tree, h, w) or check_down(tree, h, w)


for h in range(1, height - 1):
    for w in range(1, width - 1):
        if isVisible(grid[h][w], h, w):
            visible += 1


print(visible)
