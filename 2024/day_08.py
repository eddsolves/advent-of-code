import string

from itertools import combinations

map = []

with open("2024/data/day_08.test.txt", "r") as file:
    for line in file:
        map.append(line.strip())

MAP_X = len(map[0])
MAP_Y = len(map)


def detect_frequencies(map):
    frequency_map = {}

    all_characters = string.ascii_letters + string.digits

    for i, row in enumerate(map):
        for j, column in enumerate(row):
            if column in all_characters:
                if column in frequency_map:
                    frequency_map[column].append((i, j))
                else:
                    frequency_map[column] = [(i, j)]

    return frequency_map


def calculate_antinodes(antennas):
    pairs = list(combinations(antennas, 2))

    antinodes = []

    for pair in pairs:
        small_x = pair[0][0]
        small_y = pair[0][1]

        large_x = pair[1][0]
        large_y = pair[1][1]

        distance_x = large_x - small_x
        distance_y = large_y - small_y

        i = 0

        while True:
            antinode_x = small_x - (distance_x * i)
            antinode_y = small_y - (distance_y * i)

            if (antinode_x >= 0 and antinode_x < MAP_X) and (
                antinode_y >= 0 and antinode_y < MAP_Y
            ):
                antinodes.append((antinode_x, antinode_y))
                i += 1
            else:
                break

        j = 0

        while True:
            antinode_x = large_x + (distance_x * j)
            antinode_y = large_y + (distance_y * j)

            if (antinode_x >= 0 and antinode_x < MAP_X) and (
                antinode_y >= 0 and antinode_y < MAP_Y
            ):
                antinodes.append((antinode_x, antinode_y))
                j += 1
            else:
                break

    return antinodes


def solve():
    frequency_map = detect_frequencies(map)
    antinodes = []

    for _, antenna_positions in frequency_map.items():
        antinodes += calculate_antinodes(antenna_positions)

    print(set(antinodes))
    return len(set(antinodes))


print(solve())
