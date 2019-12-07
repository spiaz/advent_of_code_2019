#%%
# --- Day 4: Secure Container ---
# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?


def is_valid(n, start, end):
    if (n < start) or (n > end):
        # should be within the limits
        return False

    s = str(n)
    valid = True
    if len(s) != 6:
        # should be 6 digits
        valid = False
    elif any([a > b for a, b in zip(s[:-1], s[1:])]):
        # shouldn't be decreasing
        valid = False
    elif len([a for a, b in zip(s[:-1], s[1:]) if a == b]) == 0:
        # should have at least 2 equal adjacent numbers
        valid = False

    return valid


assert is_valid(111111, 0, 10000000)
assert not is_valid(223450, 0, 100000000)
assert not is_valid(123789, 0, 12312312)

start, end = 248345, 746315

valid = []
for i, x in enumerate(range(start, end, 1)):
    if i % 10000 == 0:
        print(f"{i} - {i / (end - start) * 100:.1f}%")
    if is_valid(x, start, end):
        valid.append(x)

print(len(valid))  # 1019
# %%
# --- Part Two ---
# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

# Given this additional criterion, but still ignoring the range rule, the following are now true:

# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
# How many different passwords within the range given in your puzzle input meet all of the criteria?

from collections import Counter


def is_valid2(n, start, end):
    if (n < start) or (n > end):
        # should be within the limits
        return False

    s = str(n)
    valid = True
    if len(s) != 6:
        # should be 6 digits
        valid = False
    elif any([a > b for a, b in zip(s[:-1], s[1:])]):
        # shouldn't be decreasing
        valid = False

    else:
        # should have a couple of consecutive numbers that is not a triplet
        c = Counter(s)
        if len([x for x, cnt in c.most_common() if cnt == 2]) == 0:
            valid = False

    return valid


assert is_valid2(112233, 0, 10000000)
assert not is_valid2(123444, 0, 100000000)
assert is_valid2(111122, 0, 10000000)
# %%
valid = []
for i, x in enumerate(range(start, end, 1)):
    if i % 100000 == 0:
        print(f"{i} - {i / (end - start) * 100:.1f}%")
    if is_valid2(x, start, end):
        valid.append(x)

print(len(valid))  # 660

# %%
