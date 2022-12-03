import string


def get_input():
    return [line.strip() for line in open("input.txt").readlines()]


def get_priority(item):
    return string.ascii_letters.find(item) + 1


def split_string_in_middle(input_string):
    return input_string[:len(input_string) // 2], input_string[len(input_string) // 2:]


def split_rucksacks_in_groups_of_3(rucksacks):
    return [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]


def find_shared_letters_between_list_of_strings(input_list):
    return set.intersection(*[set(s) for s in input_list])


input_rucksacks = get_input()


def part_1(input_rucksacks):
    total_priority = 0
    for rucksack in input_rucksacks:
        compartments = split_string_in_middle(rucksack)
        letters_in_both_rucksacks = find_shared_letters_between_list_of_strings(compartments)
        for letter in letters_in_both_rucksacks:
            total_priority += get_priority(letter)
    return total_priority


def part_2(input_rucksacks):
    total_priority = 0
    for group in split_rucksacks_in_groups_of_3(input_rucksacks):
        total_priority += get_priority(find_shared_letters_between_list_of_strings(group).pop())
    return total_priority


print("Total priority part 1:", part_1(input_rucksacks))
print("Total priority part 2:", part_2(input_rucksacks))
