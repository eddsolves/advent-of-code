def part_1():
    input = ""
    total = 0

    with open("2024/day_03.txt", "r") as f:
        for line in f:
            input += line.strip()

        for i in range(len(input)):
            if (
                input[i] == "m"
                and input[i + 1] == "u"
                and input[i + 2] == "l"
                and input[i + 3] == "("
            ):
                j = i + 4

                substring = ""

                while input[j] != ")":
                    if input[j] in [
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                        "0",
                        ",",
                    ]:
                        substring += input[j]
                        j += 1
                    else:
                        substring = ""
                        break

                if substring != "" and "," in substring:
                    x, y = substring.split(",")
                    total += int(x) * int(y)

    return total


def part_2():
    input = ""
    total = 0
    do = True

    with open("2024/day_03.txt", "r") as f:
        for line in f:
            input += line.strip()

        for i in range(len(input)):
            if do:
                if (
                    input[i] == "d"
                    and input[i + 1] == "o"
                    and input[i + 2] == "n"
                    and input[i + 3] == "'"
                    and input[i + 4] == "t"
                    and input[i + 5] == "("
                    and input[i + 6] == ")"
                ):
                    do = False
                    continue

                if (
                    input[i] == "m"
                    and input[i + 1] == "u"
                    and input[i + 2] == "l"
                    and input[i + 3] == "("
                ):
                    j = i + 4

                    substring = ""

                    while input[j] != ")":
                        if input[j] in [
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7",
                            "8",
                            "9",
                            "0",
                            ",",
                        ]:
                            substring += input[j]
                            j += 1
                        else:
                            substring = ""
                            break

                    if substring != "" and "," in substring:
                        x, y = substring.split(",")
                        total += int(x) * int(y)

            else:
                if (
                    input[i] == "d"
                    and input[i + 1] == "o"
                    and input[i + 2] == "("
                    and input[i + 3] == ")"
                ):
                    do = True
                    continue

    return total


print(part_1())
print(part_2())
