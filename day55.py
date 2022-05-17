def is_valid_IP(strng):
    print(strng)
    
    octets = strng.split(".")
    print(octets)
    if len(octets) != 4:
        return False
    
    for octet in octets:
        if octet.isnumeric() == True:
            if octet[0] == '0' and len(octet) > 1: 
                return False
            else:
                if int(octet) <= 255:
                    continue
                else:
                    return False
        else:
            return False
    
    return True