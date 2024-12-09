import itertools

def calculate_checksum(file_blocks):
    total = 0
    for i, file_block in enumerate(file_blocks):
        if file_block == ".":
            continue

        total += int(file_block) * i

    return total


def compress_by_block(file_blocks):
    limit = len(list(filter(lambda x: x != ".", file_blocks)))
    length_of_dots = len(file_blocks) - limit
    
    for i, block in enumerate(file_blocks[::-1]):
        if i > length_of_dots:
            break
        
        if block == ".":
            continue
        
        for j, block in enumerate(file_blocks):
            if block == ".":
                file_blocks[j] = file_blocks[::-1][i]
                file_blocks[::-1][i] = "."
                break
    
    
    file_blocks = file_blocks[:limit] + ["."] * length_of_dots
    
    return file_blocks

def compress_by_file(file_blocks):
    
    for i, block in enumerate(file_blocks[::-1]):
        block = block[0]
        
        if "." in block:
            continue
        
        for j, _block in enumerate(file_blocks):
            _block = _block[0]
            
            if len(_block) >= len(block) and "." in _block:
                file_blocks[j] = [block]
                break 
                        
    return file_blocks

def part_1():
    disk_map = ""
    file_blocks = []

    with open("2024/data/day_09.txt", "r") as file:
        for line in file:
            disk_map += line.strip()

    id_number = 0
    for i, _ in enumerate(disk_map):
        if i % 2 == 0:
            for _ in range(int(disk_map[i])):
                file_blocks.append(str(id_number))
            id_number += 1
        else:
            for _ in range(int(disk_map[i])):
                file_blocks.append(".")
                
    compressed_file_blocks = compress_by_block(file_blocks)

    return calculate_checksum(compressed_file_blocks)

def part_2():
    disk_map = ""
    file_blocks = []

    with open("2024/data/day_09.test.txt", "r") as file:
        for line in file:
            disk_map += line.strip()

    id_number = 0
    for i, _ in enumerate(disk_map):
        if i % 2 == 0:
            file_blocks.append([f"{id_number}" * int(disk_map[i])])
            id_number += 1
        else:
            file_blocks.append(["." * int(disk_map[i])])

    print(file_blocks)
    compressed_file_blocks = compress_by_file(file_blocks)
    compressed_file_blocks = "".join(list(itertools.chain(*compressed_file_blocks)))
    print(compressed_file_blocks)
    #print(compressed_file_blocks)
    #return calculate_checksum(compressed_file_blocks)

# print(part_1())
print(part_2())
