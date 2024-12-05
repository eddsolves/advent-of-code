def is_valid(update, rules) -> bool:        
    for i, page in enumerate(update):
        if page in rules:
            invalid_previous_pages = rules[page]
            if any(p for p in invalid_previous_pages if p in update[:i]):
                return False
    
    return True

def part_1():
    total = 0
    
    page_rules = {}
    updates = []
    with open("2024/data/day_05.txt", "r") as file:
        for line in file:
            if '|' in line:
                page, rule = line.strip().split('|')
                if page in page_rules:
                    page_rules[page].append(rule)
                else:
                    page_rules[page] = [rule]
            elif ',' in line:
                updates.append(line.strip().split(','))
    
    for update in updates:      
        if is_valid(update, page_rules):
            total += int(update[len(update) // 2])

    return total

def part_2():
    total = 0
    
    page_rules = {}
    updates = []
    with open("2024/data/day_05.txt", "r") as file:
        for line in file:
            if '|' in line:
                page, rule = line.strip().split('|')
                if page in page_rules:
                    page_rules[page].append(rule)
                else:
                    page_rules[page] = [rule]
            elif ',' in line:
                updates.append(line.strip().split(','))
    
    invalid_updates = []
    
    for update in updates:        
        if not is_valid(update, page_rules):
            invalid_updates.append(update)

    for invalid_update in invalid_updates:
        while not is_valid(invalid_update, page_rules):
            for i, page in enumerate(invalid_update):
                if page in page_rules:
                    invalid_pages = page_rules[page]
                    
                    j = 0
                    while j < i:
                        if invalid_update[j] in invalid_pages:
                            temp_i = invalid_update[i]
                            temp_j = invalid_update[j]
                            invalid_update[i] = temp_j
                            invalid_update[j] = temp_i
                        j += 1
        
        total += int(invalid_update[len(invalid_update) // 2])
    return total

print(part_1())
print(part_2())
