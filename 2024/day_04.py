word_search = []

with open("2024/data/day_04.txt", "r") as file:
    for line in file:
        word_search.append(line.strip())

X_LIMIT = len(word_search[0]) - 1
Y_LIMIT = len(word_search) - 1


def check_right(word_search, x, y) -> bool:
    if x + 3 > X_LIMIT:
        return False

    return all(
        [
            word_search[y][x] == "X",
            word_search[y][x + 1] == "M",
            word_search[y][x + 2] == "A",
            word_search[y][x + 3] == "S",
        ]
    )


def check_left(word_search, x, y) -> bool:
    if x - 3 < 0:
        return False

    return all(
        [
            word_search[y][x] == "X",
            word_search[y][x - 1] == "M",
            word_search[y][x - 2] == "A",
            word_search[y][x - 3] == "S",
        ]
    )


def check_up(word_search, x, y) -> bool:
    if y - 3 < 0:
        return False

    return all(
        [
            word_search[y][x] == "X",
            word_search[y - 1][x] == "M",
            word_search[y - 2][x] == "A",
            word_search[y - 3][x] == "S",
        ]
    )


def check_down(word_search, x, y) -> bool:
    if y + 3 > Y_LIMIT:
        return False

    return all(
        [
            word_search[y][x] == "X",
            word_search[y + 1][x] == "M",
            word_search[y + 2][x] == "A",
            word_search[y + 3][x] == "S",
        ]
    )


def check_diagonally_up_right(word_search, x, y) -> bool:
    if x + 3 > X_LIMIT or y - 3 < 0:
        return False

    return all(
        [
            word_search[y][x] == "X",
            word_search[y - 1][x + 1] == "M",
            word_search[y - 2][x + 2] == "A",
            word_search[y - 3][x + 3] == "S",
        ]
    )


def check_diagonally_up_left(word_search, x, y) -> bool:
    if x - 3 < 0 or y - 3 < 0:
        return False

    return all(
        [
            word_search[y][x] == "X",
            word_search[y - 1][x - 1] == "M",
            word_search[y - 2][x - 2] == "A",
            word_search[y - 3][x - 3] == "S",
        ]
    )


def check_diagonally_down_right(word_search, x, y) -> bool:
    if x + 3 > X_LIMIT or y + 3 > Y_LIMIT:
        return False

    return all(
        [
            word_search[y][x] == "X",
            word_search[y + 1][x + 1] == "M",
            word_search[y + 2][x + 2] == "A",
            word_search[y + 3][x + 3] == "S",
        ]
    )


def check_diagonally_down_left(word_search, x, y) -> bool:
    if x - 3 < 0 or y + 3 > Y_LIMIT:
        return False

    return all(
        [
            word_search[y][x] == "X",
            word_search[y + 1][x - 1] == "M",
            word_search[y + 2][x - 2] == "A",
            word_search[y + 3][x - 3] == "S",
        ]
    )


def part_1(word_search):
    count = 0

    for y in range(len(word_search)):
        for x in range(len(word_search)):
            if check_up(word_search, x, y):
                count += 1
            if check_diagonally_up_right(word_search, x, y):
                count += 1
            if check_right(word_search, x, y):
                count += 1
            if check_diagonally_down_right(word_search, x, y):
                count += 1
            if check_down(word_search, x, y):
                count += 1
            if check_diagonally_down_left(word_search, x, y):
                count += 1
            if check_left(word_search, x, y):
                count += 1
            if check_diagonally_up_left(word_search, x, y):
                count += 1

    return count


def check_for_mas(word_search, x, y) -> bool:
    if any([x - 1 < 0, x + 1 > X_LIMIT, y - 1 < 0, y + 1 > Y_LIMIT]):
        return False
    
    if word_search[y][x] != "A":
        return False

    #            X
    #        -1  0 +1
    #   -1 |  M     M
    # Y  0 |     A
    #   +1 |  S     S

    if (
        word_search[y - 1][x - 1] == "M"
        and word_search[y - 1][x + 1] == "M"
        and word_search[y + 1][x + 1] == "S"
        and word_search[y + 1][x - 1] == "S"
    ):
        return True

    #            X
    #        -1  0 +1
    #   -1 |  S     S
    # Y  0 |     A
    #   +1 |  M     M

    if (
        word_search[y - 1][x - 1] == "S"
        and word_search[y - 1][x + 1] == "S"
        and word_search[y + 1][x + 1] == "M"
        and word_search[y + 1][x - 1] == "M"
    ):
        return True

    #            X
    #        -1  0 +1
    #   -1 |  M     S
    # Y  0 |     A
    #   +1 |  M     S

    if (
        word_search[y - 1][x - 1] == "M"
        and word_search[y - 1][x + 1] == "S"
        and word_search[y + 1][x + 1] == "S"
        and word_search[y + 1][x - 1] == "M"
    ):
        return True

    #            X
    #        -1  0 +1
    #   -1 |  S     M
    # Y  0 |     A
    #   +1 |  S     M

    if (
        word_search[y - 1][x - 1] == "S"
        and word_search[y - 1][x + 1] == "M"
        and word_search[y + 1][x + 1] == "M"
        and word_search[y + 1][x - 1] == "S"
    ):
        return True

    return False


def part_2(word_search):
    count = 0

    for y in range(len(word_search)):
        for x in range(len(word_search)):
            if check_for_mas(word_search, x, y):
                count += 1

    return count


print(part_1(word_search))
print(part_2(word_search))
