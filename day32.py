def what_century(year):
    suffix = {1: "st", 2: "nd", 3: "rd", 4: 'th'}
    century = ""
    first_half = f"{year[0]}{year[1]}"
    second_half = f"{year[2]}{year[3]}"
    
    if int(second_half) > 0:
        century += str(int(first_half) + 1)
    else:
        century += first_half
    
    if century[1] == "1" and int(century) != 11:
        century += suffix[1]
    elif century[1] == "2" and int(century) != 12:
        century += suffix[2]
    elif century[1] == "3" and int(century) != 13:
        century += suffix[3]
    else:
        century += suffix[4]
          
    return century