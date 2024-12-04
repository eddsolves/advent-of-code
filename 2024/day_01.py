def part_1():
    count = 0
    left_side = []
    right_side = []

    with open("./2024/data/day_01.txt", "r") as f:
        for line in f:
            ls, rs = map(int, line.split())
            left_side.append(ls)
            right_side.append(rs)

    left_side.sort()
    right_side.sort()

    for i, val in enumerate(left_side):
        count += abs(val - right_side[i])

    return count


def part_2():
    count = 0
    left_side = []
    right_side = []

    with open("./2024/data/day_01.txt", "r") as f:
        for line in f:
            ls, rs = map(int, line.split())
            left_side.append(ls)
            right_side.append(rs)

    left_side.sort()
    right_side.sort()

    similarity_score = {}

    for value in right_side:
        if value in similarity_score:
            similarity_score[value] += 1
        else:
            similarity_score[value] = 1

    for value in left_side:
        if value in similarity_score:
            count += value * similarity_score[value]

    return count


print(part_1())
print(part_2())
