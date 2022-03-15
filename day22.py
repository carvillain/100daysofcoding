def find_senior(lst): 
    senior_developers = []
    max_age = 0
    
    for item in lst:
        if item['age'] > max_age:
            max_age = item['age']
    
    for dev in lst:
        if dev['age'] == max_age:
            senior_developers.append(dev)
    
    return senior_developers