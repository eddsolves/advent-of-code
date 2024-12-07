from itertools import product


def part_1():
    total = 0
    inputs = {}

    with open("2024/data/day_07.txt", "r") as file:
        for line in file:
            target, values = line.strip().split(":")
            inputs[int(target)] = list(map(int, values.strip().split(" ")))

    for target, values in inputs.items():
        totals = {}

        all_operations = list(
            map(list, product(["sum", "mult"], repeat=len(values) - 1))
        )

        for operations in all_operations:
            running_total = values[0]
            for i, operation in enumerate(operations):
                match operation:
                    case "sum":
                        running_total += values[i + 1]
                    case "mult":
                        running_total *= values[i + 1]

            totals[running_total] = (operations, values)

        if target in totals:
            total += target

    return total


print(part_1())
