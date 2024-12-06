seen_locations = {}

def new_map():
    map = []
    
    with open("2024/data/day_06.txt", "r") as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            map.append(row)
            
    return map 

def get_guard_position(map):
    for y, row in enumerate(map):
        for x, row in enumerate(row):
            if map[y][x] in ['^', '>', '<', 'v']:
                return (x, y)

def rotate_guard(map, y, x):
    direction = map[y][x]

    match direction:
        case '^':
            map[y][x] = '>'
        case '>':
            map[y][x] = 'v'
        case 'v':
            map[y][x] = '<'
        case '<':
            map[y][x] = '^'

def move(map, x, y):
    seen_locations[(y,x)] = True
    direction = map[y][x]
    
    match direction:
        case '^':
            if map[y-1][x] != '#':
                map[y-1][x] = '^'
                map[y][x] = '.'
                return (x, y-1)
            else:
                rotate_guard(map, y, x)
                return(x, y)
                
        case '>':
            if map[y][x+1] != '#':
                map[y][x+1] = '>'
                map[y][x] = '.'
                return (x+1, y)
            else:
                rotate_guard(map, y, x)
                return(x, y)
                
        case 'v':
            if map[y+1][x] != '#':
                map[y+1][x] = 'v'
                map[y][x] = '.'
                return (x, y+1)  
            else:
                rotate_guard(map, y, x)
                return (x, y)
                      
        case '<':
            if map[y][x-1] != '#':
                map[y][x-1] = '<'
                map[y][x] = '.'
                return (x-1, y)
            else:
                rotate_guard(map, y, x)
                return (x, y)

def has_escaped(map, x, y) -> bool:
    seen_locations[(y,x)] = True
    direction = map[y][x]
    
    match direction:
        case '^':
            if y == 0:
                return True
            else:
                return False       
        case '>':
            if x == (len(map[0]) - 1):
                return True
            else:
                return False    
        case 'v':
            if y == len(map) - 1:
                return True
            else:
                return False         
        case '<':
            if x == 0:
                return True
            else:
                return False 
            
def add_obstruction(map, x, y):
    if map[y][x] not in ['^', '>', 'v', '<', '#']:
        map[y][x] = '#'    
    
def remove_obstruction(map, y, x):
    if map[y][x] == '#':
        map[y][x] = '.'   

def part_1():
    map = new_map()
    
    while not has_escaped(map):
        move(map)
    
    return len(seen_locations)

def part_2():
    map = new_map()

    count = 0
    for y, row in enumerate(map):
        for x, _ in enumerate(row):
            print(f"Trying x:{x} y:{y}")
            add_obstruction(map, x, y)
            turns = 0
            
            gx, gy = get_guard_position(map)

            while not has_escaped(map, gx, gy):
                gx, gy = move(map, gx, gy)
                turns += 1
                
                # Why cycle when you can brute?
                if turns == 10_000:
                    count += 1
                    print(f"Found {count}!")
                    break
            
            # Reset map
            map = new_map()

    return count

print(part_1())
print(part_2())