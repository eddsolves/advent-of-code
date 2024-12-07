from itertools import product


def solve():
    total = 0
    targets = []
    allvalues = []

    with open("2024/data/day_07.txt", "r") as file:
        for line in file:
            target, values = line.strip().split(":")
            targets.append(int(target))
            allvalues.append(list(map(int, values.strip().split(" "))))

    for target, values in zip(targets, allvalues):
        all_operations = product(['sum', 'mult', 'concat'], repeat=len(values) - 1)
        for operations in all_operations:
            running_total = values[0]
            found_concat = False
            for i, operation in enumerate(operations):
                match operation:
                    case "sum":
                        running_total += values[i + 1]
                    case "mult":
                        running_total *= values[i + 1]
                    case "concat":
                        running_total = int(str(running_total) + str(values[i+1]))

                        
            if running_total == target and not found_concat:
                total += target
                break

    return total


print(solve())
