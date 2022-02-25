def inverse_slice(items, a, b):
    altered_items_list = []
    
    for i in range(len(items)):
        if i not in range(a, b):
            altered_items_list.append(items[i])
        
    return altered_items_list