from collections import namedtuple

Move = namedtuple('Move', 'amount from_crate to_crate')


def get_input():
    crate_input, move_input = open("input.txt").read().split("\n\n")
    return crate_input, move_input


def get_crates(crate_input):
    rows = crate_input.splitlines()[:-1]
    rows.reverse()

    crates = {}

    for row in rows:
        crate_index = 0
        for i in range(1, len(row) - 1, 4):
            crate_index += 1
            if row[i] == " ":
                continue

            if crate_index not in crates:
                crates[crate_index] = []

            crate = crates[crate_index]
            crate.append(row[i])
            crates[crate_index] = crate

    return crates


def get_moves(move_input):
    move_inputs = move_input.splitlines()
    moves = []
    for move in move_inputs:
        move = move.split()
        moves.append(Move(int(move[1]), int(move[3]), int(move[5])))
    return moves


def do_move(crates, move):
    for i in range(move.amount):
        crates[move.to_crate].append(crates[move.from_crate].pop())
    return crates


def do_move_stack(crates, move):
    stack = []
    for i in range(move.amount):
        stack.append(crates[move.from_crate].pop())

    stack.reverse()
    crates[move.to_crate].extend(stack)


def move_all(crates, moves):
    for move in moves:
        crates = do_move(crates, move)
    return crates


def move_all_stack(crates, moves):
    for move in moves:
        do_move_stack(crates, move)
    return crates


def part_1(crate_input, move_input):
    crates = get_crates(crate_input)
    moves = get_moves(move_input)
    crates = move_all(crates, moves)
    print("".join([crate.pop() for crate in crates.values()]))


def part_2(crate_input, move_input):
    crates = get_crates(crate_input)
    moves = get_moves(move_input)
    crates = move_all_stack(crates, moves)
    print("".join([crate.pop() for crate in crates.values()]))


if __name__ == "__main__":
    crate_input, move_input = get_input()
    part_1(crate_input, move_input)
    part_2(crate_input, move_input)
