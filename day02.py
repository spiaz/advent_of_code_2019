#%%
from typing import NamedTuple, Optional


def parse_str(s):
    return [int(x) for x in s.split(",")]


class Result(NamedTuple):
    code: int
    s: str


def run_operations(ops):
    ip = 0
    while ip < len(ops):
        opcode = ops[ip]
        if opcode == 99:
            break
        p1 = ops[ip + 1]
        p2 = ops[ip + 2]
        p3 = ops[ip + 3]
        if opcode == 1:
            # Opcode 1 adds together numbers read from two
            # positions and stores the result in a third position.
            ops[p3] = ops[p1] + ops[p2]
        elif opcode == 2:
            # Opcode 2 multiplies the two inputs instead of adding them.
            ops[p3] = ops[p1] * ops[p2]
        ip += 4

    return Result(ops[0], ",".join([str(x) for x in ops]))


assert run_operations(parse_str("1,0,0,0,99")).s == "2,0,0,0,99"
assert run_operations(parse_str("2,3,0,3,99")).s == "2,3,0,6,99"
assert run_operations(parse_str("2,4,4,5,99,0")).s == "2,4,4,5,99,9801"
assert run_operations(parse_str("1,1,1,4,99,5,6,0,99")).s == "30,1,1,4,2,5,6,0,99"

# %%
with open("day02_input.txt", "r") as f:
    line = f.read()


def restore_program_alarm(s, noun, verb):
    # replace position 1 with the value noun
    # and replace position 2 with the value verb
    s[1] = noun
    s[2] = verb
    return s


s = parse_str(line)
print(run_operations(restore_program_alarm(s, 12, 2)).code)  # 9581917

# %%

# ----------------------------------- Part 2 --------------------------------- #
desired = 19690720

with open("day02_input.txt", "r") as f:
    line = f.read()
line

s = parse_str(line)

for i, (noun, verb) in enumerate(
    [(noun, verb) for verb in range(100) for noun in range(100)]
):
    ss = s.copy()
    val = run_operations(restore_program_alarm(ss, noun, verb)).code
    if val == desired:
        print(100 * noun + verb)  # 2505
        break
