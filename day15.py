def order_food(lst): 
    new_dict = {}
    
    for x in lst:
        if x['meal'] not in new_dict.keys():
            new_dict[x['meal']] = 1
        else:
            new_dict[x['meal']] += 1
    return new_dict