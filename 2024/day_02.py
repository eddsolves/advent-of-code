def is_safe_ascending(level) -> bool:
    lower_limit = 1
    upper_limit = 3

    for i, report in enumerate(level):
        if i == 0:
            continue
        if lower_limit <= report - level[i - 1] <= upper_limit:
            continue
        else:
            return False

    return True


def is_safe_descending(level) -> bool:
    lower_limit = 1
    upper_limit = 3

    for i, report in enumerate(level):
        if i == 0:
            continue
        if lower_limit <= level[i - 1] - report <= upper_limit:
            continue
        else:
            return False

    return True


def part_1():
    count = 0
    levels = []

    with open("./2024/day_02.txt", "r") as f:
        for line in f:
            levels.append(list(map(int, line.strip().split(" "))))

    for level in levels:
        if is_safe_ascending(level) or is_safe_descending(level):
            count += 1

    return count


# Nothing about this is nice
def part_2():
    count = 0
    levels = []

    with open("./2024/day_02.txt", "r") as f:
        for line in f:
            levels.append(list(map(int, line.strip().split(" "))))

    for level in levels:
        if is_safe_ascending(level) or is_safe_descending(level):
            count += 1
            continue

        for i in range(len(level)):
            temp_level = level[:i] + level[i + 1 :]
            if is_safe_ascending(temp_level) or is_safe_descending(temp_level):
                count += 1
                break

    return count


print(part_1())
print(part_2())
