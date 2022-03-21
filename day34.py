def delete_nth(order,max_e):
    new_order = []
    
    for item in order:
        if new_order.count(item) < max_e:
            new_order.append(item)
    
    return new_order