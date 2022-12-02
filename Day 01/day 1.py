input_data = open("Day 01/input.txt").readlines()

elf_calorie_counts = []
current_calorie_count = 0
for row in input_data:
    if row == '\n':
        elf_calorie_counts.append(current_calorie_count)
        current_calorie_count = 0
    else:
        current_calorie_count += int(row)

print("Max value:", max(elf_calorie_counts))

elf_calorie_counts.sort()
print("Top 3 value:", sum(elf_calorie_counts[-3:]))
