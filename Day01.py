#%%
import numpy as np


def get_fuel(mass):
    return np.floor(mass / 3) - 2


assert get_fuel(12) == 2
assert get_fuel(14) == 2.0
assert get_fuel(1969) == 654
assert get_fuel(100756) == 33583.0


# %%
with open("Day01_input.txt", "r") as f:
    masses = [int(x.strip()) for x in f.readlines()]

fuels = [get_fuel(m) for m in masses]
np.sum(fuels)
# %%


def total_fuel(m):
    fuels = []
    while get_fuel(m) > 0:
        m = get_fuel(m)
        fuels.append(m)
    return sum(fuels)


assert total_fuel(14) == 2.0
assert total_fuel(1969) == 966.0
assert total_fuel(100756) == 50346

# %%
with open("Day01_input2.txt", "r") as f:
    masses = [int(x.strip()) for x in f.readlines()]

fuels = [total_fuel(m) for m in masses]
np.sum(fuels)
