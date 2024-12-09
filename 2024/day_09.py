def calculate_checksum(file_blocks):
    total = 0
    for i, file_block in enumerate(file_blocks):
        if file_block == ".":
            continue

        total += int(file_block) * i

    return total


def compress(file_blocks):
    limit = len(list(filter(lambda x: x != ".", list(file_blocks))))
    print(limit)
    file_blocks = list(file_blocks)

    for i, block in enumerate(file_blocks[::-1]):
        if block == ".":
            continue

        for j, block in enumerate(file_blocks):
            if block == ".":
                file_blocks[j] = file_blocks[::-1][i]
                file_blocks[::-1][i] = "."
                break

    for i, block in enumerate(file_blocks):
        if i >= limit:
            file_blocks[i] = "."

    return "".join(file_blocks)


def part_1():
    disk_map = ""
    file_blocks = ""

    with open("2024/data/day_09.txt", "r") as file:
        for line in file:
            disk_map += line.strip()

    id_number = 0
    for i, _ in enumerate(disk_map):
        if i % 2 == 0:
            for _ in range(int(disk_map[i])):
                file_blocks += str(id_number)
            id_number += 1
        else:
            for _ in range(int(disk_map[i])):
                file_blocks += "."

    compressed_file_blocks = compress(file_blocks)

    return calculate_checksum(compressed_file_blocks)


print(part_1())
