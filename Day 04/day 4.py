def get_input():
    return [line.strip() for line in open("input.txt").readlines()]


def get_pairs(input_list):
    return [item.split(",") for item in input_list]


def get_ranges(string_range):
    return [int(item) for item in string_range.split("-")]


def check_if_range_fully_contains_other_range(range_1, range_2):
    return range_1[0] <= range_2[0] and range_1[1] >= range_2[1]


def check_if_range_partially_contains_other_range(range_1, range_2):
    return range_1[0] <= range_2[0] <= range_1[1] or range_1[0] <= range_2[1] <= range_1[1]


def part_1(input_list):
    overlapping_ranges = 0
    for pair in get_pairs(input_list):
        range1 = get_ranges(pair[0])
        range2 = get_ranges(pair[1])
        if check_if_range_fully_contains_other_range(range1, range2):
            overlapping_ranges += 1
        elif check_if_range_fully_contains_other_range(range2, range1):
            overlapping_ranges += 1
    return overlapping_ranges


def part_2(input_list):
    overlapping_ranges = 0
    for pair in get_pairs(input_list):
        range1 = get_ranges(pair[0])
        range2 = get_ranges(pair[1])
        if check_if_range_partially_contains_other_range(range1, range2):
            overlapping_ranges += 1
        elif check_if_range_partially_contains_other_range(range2, range1):
            overlapping_ranges += 1
    return overlapping_ranges


if __name__ == "__main__":
    input_list = get_input()
    print("Overlapping ranges:", part_1(input_list))
    print("Overlapping ranges:", part_2(input_list))

