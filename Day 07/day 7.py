import pathlib


def get_input():
    return [line.strip() for line in open("input.txt").readlines()]


def get_directory_sizes(input, base_path):
    current_path = base_path
    sizes = {}
    for line in input:
        if line == "$ cd /":
            current_path = base_path
            continue

        if line == "$ cd ..":
            current_path = current_path.parent
            continue

        if line.startswith("$ cd "):
            current_path /= line.replace("$ cd ", "")
            continue

        if line.startswith("$ ls"):
            continue

        if line.startswith("dir "):
            continue

        amount_bytes, filename = line.split(" ")
        amount_bytes = int(amount_bytes)

        if current_path not in sizes:
            sizes[current_path] = 0

        sizes[current_path] += amount_bytes
        for path in current_path.parents:
            if path not in sizes:
                sizes[path] = 0
            sizes[path] += amount_bytes
    return sizes



if __name__ == "__main__":
    input_text = get_input()
    sizes = get_directory_sizes(input_text, pathlib.Path("/"))
    base = pathlib.Path("/")
    print("part 1:", (sum([val if val <= 100000 else 0 for val in sizes.values()])))
    size_root = sizes[base]
    free_space = 70000000 - size_root
    needed_space = 30000000 - free_space
    print("part 2:", min([val for val in sizes.values() if val >= needed_space]))
