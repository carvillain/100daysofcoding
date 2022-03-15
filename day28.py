def find_outlier(list):
    for i in range(len(list)):
        if list[0] % 2 == 0 and list[1] % 2 == 0:
            for i in list:
                if i % 2 !=0:
                    return i
        elif list[0] % 2 != 0 and list[1] % 2 != 0:
            for i in list:
                if i % 2 == 0:
                    return i
        else:
            if list[2] % 2 == 0:
                if list[0] % 2 != 0:
                    return list[0]
                else:
                    return list[1]
            else:
                if list[0] % 2 != 0:
                    return list[1]
                else:
                    return list[0]