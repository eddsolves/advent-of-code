def check_right(word_search, x, y) -> bool:
    try:
        return all(
            [
                word_search[y][x] == "X",
                word_search[y][x + 1] == "M",
                word_search[y][x + 2] == "A",
                word_search[y][x + 3] == "S",
            ]
        )
    except Exception as e:
        return False


def check_left(word_search, x, y) -> bool:
    try:
        return all(
            [
                word_search[y][x] == "X",
                word_search[y][x - 1] == "M",
                word_search[y][x - 2] == "A",
                word_search[y][x - 3] == "S",
            ]
        )
    except Exception as e:
        return False


def check_up(word_search, x, y) -> bool:
    try:
        return all(
            [
                word_search[y][x] == "X",
                word_search[y + 1][x] == "M",
                word_search[y + 2][x] == "A",
                word_search[y + 3][x] == "S",
            ]
        )
    except Exception as e:
        return False


def check_down(word_search, x, y) -> bool:
    try:
        return all(
            [
                word_search[y][x] == "X",
                word_search[y - 1][x] == "M",
                word_search[y - 2][x] == "A",
                word_search[y - 3][x] == "S",
            ]
        )
    except Exception as e:
        return False


def check_diagonally_up_right(word_search, x, y) -> bool:
    try:
        return all(
            [
                word_search[y][x] == "X",
                word_search[y + 1][x + 1] == "M",
                word_search[y + 2][x + 2] == "A",
                word_search[y + 3][x + 3] == "S",
            ]
        )
    except Exception as e:
        return False


def check_diagonally_up_left(word_search, x, y) -> bool:
    try:
        return all(
            [
                word_search[y][x] == "X",
                word_search[y + 1][x - 1] == "M",
                word_search[y + 2][x - 2] == "A",
                word_search[y + 3][x - 3] == "S",
            ]
        )
    except Exception as e:
        return False


def check_diagonally_down_right(word_search, x, y) -> bool:
    try:
        return all(
            [
                word_search[y][x] == "X",
                word_search[y - 1][x + 1] == "M",
                word_search[y - 2][x + 2] == "A",
                word_search[y - 3][x + 3] == "S",
            ]
        )
    except Exception as e:
        return False


def check_diagonally_down_left(word_search, x, y) -> bool:
    try:
        return all(
            [
                word_search[y][x] == "X",
                word_search[y - 1][x - 1] == "M",
                word_search[y - 2][x - 2] == "A",
                word_search[y - 3][x - 3] == "S",
            ]
        )
    except Exception as e:
        return False


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


if __name__ == "__main__":
    word_search = []

    with open("2024/day_04.test.txt", "r") as file:
        for line in file:
            word_search.append(line.strip())

    print(part_1(word_search))
