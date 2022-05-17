def tower_builder(n_floors):
    floors = []
    
    current_floor = 1
    
    while current_floor <= n_floors:
        floor = ""
        total_length = n_floors * 2 - 1
        stars = current_floor * 2 - 1
        spaces = total_length - stars
        half_spaces = int(spaces / 2)
        
        if stars == total_length:
            floor += "".join(["*"] * stars)
        
        else:
            floor += "".join([" "] * half_spaces)
            floor += "".join(["*"] * stars)
            floor += "".join([" "] * half_spaces)
        
        floors.append(floor)
        current_floor += 1
    
    return floors