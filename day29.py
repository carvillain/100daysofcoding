def data_reverse(data):
    data_chunks = {}
    
    number_of_chunks = len(data) / 8
    
    current_chunk = 1
    
    reversed_data = []
    
    
    while current_chunk <= number_of_chunks:
        index = 0
        chunk = []
        for x in data:
            chunk.append(data[index])
            index += 1

            if index % 8 == 0:
                data_chunks[current_chunk] = chunk
                current_chunk += 1
                chunk = []
    
    while number_of_chunks > 0:
        for x in data_chunks[number_of_chunks]:
            reversed_data.append(x)
        
        number_of_chunks -= 1
    
    return reversed_data