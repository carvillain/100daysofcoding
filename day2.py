def quarter_of(month):
    if month % 3 == 0:
        return month // 3
    else:
        return int(month // 3) + 1