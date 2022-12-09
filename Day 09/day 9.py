import math
from collections import namedtuple


def get_input():
    return open("input.txt").read()


input = get_input()

Point = namedtuple("Point", "x y")

head = Point(0, 0)
tails = [Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0),
         Point(0, 0)]

tail_visited_points = set(tails[0])


def distance_between_points(point1, point2):
    return int(math.hypot(point2.x - point1.x, point2.y - point1.y))


def move_tail(head, tail):
    if head.x == tail.x:
        difference = head.y - tail.y
        if difference < 0:
            difference += 1
        else:
            difference -= 1
        return Point(tail.x, tail.y + difference)
    if head.y == tail.y:
        difference = head.x - tail.x
        if difference < 0:
            difference += 1
        else:
            difference -= 1
        return Point(tail.x + difference, tail.y)
    if distance_between_points(head, Point(tail.x + 1, tail.y + 1)) < 2:
        return Point(tail.x + 1, tail.y + 1)
    if distance_between_points(head, Point(tail.x - 1, tail.y - 1)) < 2:
        return Point(tail.x - 1, tail.y - 1)
    if distance_between_points(head, Point(tail.x + 1, tail.y - 1)) < 2:
        return Point(tail.x + 1, tail.y - 1)
    if distance_between_points(head, Point(tail.x - 1, tail.y + 1)) < 2:
        return Point(tail.x - 1, tail.y + 1)


def move(head, tails, input_move):
    direction, amount = input_move.split(" ")
    amount = int(amount)

    for x in range(amount):
        if direction == "R":
            head = Point(head.x + 1, head.y)
        if direction == "L":
            head = Point(head.x - 1, head.y)
        if direction == "U":
            head = Point(head.x, head.y + 1)
        if direction == "D":
            head = Point(head.x, head.y - 1)

        for tail_num, tail in enumerate(tails):
            if tail_num == 0:
                prev_tail = head
            else:
                prev_tail = tails[tail_num - 1]
            if distance_between_points(prev_tail, tail) > 1:
                tails[tail_num] = move_tail(prev_tail, tail)
        tail_visited_points.add(tails[-1])
    return head, tails


for m in input.splitlines():
    head, tails = move(head, tails, m)

print(head, tails)
print(len(tail_visited_points))
