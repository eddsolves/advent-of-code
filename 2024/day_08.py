import string

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

def part_1():
    
    antinodes = 0
    map = []
    
    with open("2024/data/day_08.test.txt", "r") as file:
        for line in file:
            map.append(line.strip())
    
    frequency_map = detect_frequencies(map)
    
    print(frequency_map)
    
    return antinodes

print(part_1())