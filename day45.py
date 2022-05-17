def is_valid_walk(walk):
    home = [0,0]
    position = [0,0]
    
    if len(walk) != 10:
        return False
    
    for direction in walk:
        if direction == "n":
            position[0] += 1
        elif direction == 's':
            position[0] -= 1
        elif direction == 'w':
            position[1] -= 1
        elif direction == 'e':
            position[1] += 1
        else:
            return f"{direction} is not a cardinal direction"
        
    if position == home:
        return True
    else:
        return False