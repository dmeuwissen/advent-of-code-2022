import numpy as np


def get_input():
    return open("input.txt").read()


def get_data():
    input_list = [list(line) for line in get_input().splitlines()]
    return np.array(input_list)


def is_visible(data, x, y):
    value = data[y, x]
    if y == 0 or x == 0:
        return True
    if y == len(data[0]) - 1 or x == len(input) - 1:
        return True
    if value > max(data[:y, x]):
        return True
    if value > max(data[y + 1:, x]):
        return True
    if value > max(data[y, :x]):
        return True
    if value > max(data[y, x + 1:]):
        return True

    return False


def get_scenic_score(data, x, y):
    up, down, left, right = 0, 0, 0, 0
    self_height = data[y, x]
    for row in reversed(data[:y, x]):
        up += 1
        if row >= self_height:
            break
    for row in data[y + 1:, x]:
        down += 1
        if row >= self_height:
            break
    for row in reversed(data[y, :x]):
        left += 1
        if row >= self_height:
            break
    for row in data[y, x + 1:]:
        right += 1
        if row >= self_height:
            break

    return up * down * left * right


def part_1(data):
    visible = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if is_visible(data, x, y):
                visible += 1
    return visible


def part_2(data):
    max_score = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            score = get_scenic_score(data, x, y)
            if score > max_score:
                max_score = score
    return max_score


if __name__ == "__main__":
    input = get_data()
    print("Part 1:", part_1(input))
    print("Part 2:", part_2(input))
