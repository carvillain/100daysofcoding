def merge(*dicts):
    merged_dictionary = {}
    
    for dictionary in dicts:
        for key, value in dictionary.items():
            if key in merged_dictionary:
                merged_dictionary[key].append(value)
            else:
                merged_dictionary[key] = [value]

    return merged_dictionary