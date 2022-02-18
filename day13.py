def remove_consecutive_duplicates(s):
    lists = s.split(" ")
    s2 = ""
    for i in range(len(lists)):
        if lists[i] != lists[i-1] or i == 0:
            s2 += lists[i] + " "
    return s2.strip()