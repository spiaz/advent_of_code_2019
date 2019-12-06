#%%
from typing import NamedTuple
from dataclasses import dataclass
from collections import Counter


@dataclass
class Position:
    x: int = 0
    y: int = 0
    steps: int = 0

    def move(self, direction: str):
        self.steps += 1
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        return (self.x, self.y)


def get_path(s: str):
    moves = s.strip().split(",")
    pos = Position()
    path = []

    for move in moves:
        direction = move[0]
        n = int(move[1:])
        for _ in range(n):
            path.append(pos.move(direction))

    return path


def find_crosses_min_distance(s1, s2):
    p1 = set(get_path(s1))
    p2 = set(get_path(s2))

    cross = list(p1.intersection(p2))

    dist = sorted([abs(x) + abs(y) for x, y in cross])

    return dist[0]


assert find_crosses_min_distance("R8,U5,L5,D3", "U7,R6,D4,L4") == 6

assert (
    find_crosses_min_distance(
        "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"
    )
    == 159
)

assert (
    find_crosses_min_distance(
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    )
    == 135
)

# %%
with open("day03_input.txt", "r") as f:
    lines = f.readlines()

find_crosses_min_distance(lines[0], lines[1])  # 731

# %%


def find_crosses_min_steps(s1, s2):
    p1 = get_path(s1)
    p2 = get_path(s2)

    def steps_dict(p):
        d = {}
        for step, pos in enumerate(p, start=1):
            if pos not in d.keys():
                d[pos] = step
        return d

    d1 = steps_dict(p1)
    d2 = steps_dict(p2)

    cross = [d1[pos] + d2[pos] for pos in d1.keys() if pos in d2.keys()]

    x = sorted(cross)[0]
    return x


assert (
    find_crosses_min_steps(
        "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"
    )
    == 610
)
assert (
    find_crosses_min_steps(
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    )
    == 410
)
#%%

with open("day03_input.txt", "r") as f:
    lines = f.readlines()

find_crosses_min_steps(lines[0], lines[1])  # 22530


# %%
